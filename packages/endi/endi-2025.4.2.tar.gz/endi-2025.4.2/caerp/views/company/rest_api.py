import logging
from caerp.consts.permissions import PERMISSIONS
from typing import Dict, Iterable, List, Optional, Union, Tuple

import colander
import deform
from sqlalchemy import (
    inspect,
    or_,
    asc,
    desc,
)
from sqlalchemy.orm import load_only

from caerp.forms.company import (
    DECIMAL_TO_DISPLAY_VALUES,
    get_company_schema,
    get_mapsearch_schema,
)
from caerp.forms.jsonschema import convert_to_jsonschema
from caerp.forms.user import (
    get_antenne_options,
    get_users_options,
)
from caerp.forms.files import (
    ImageNode,
    FileUploadSchema,
    get_file_upload_preparer,
    deferred_parent_id_validator,
)
from caerp.utils.image import (
    ImageResizer,
    ImageRatio,
)
from caerp.models import DBBASE
from caerp.models.company import (
    Company,
    CompanyActivity,
)
from caerp.models.files import File
from caerp.models.user.user import User
from caerp.models.user.login import ACCOUNT_TYPES, Login
from caerp.utils.rest import (
    LoadOptions,
    PaginationOptions,
    RestCollectionMetadata,
    RestCollectionResponse,
    RestError,
    SortOptions,
)
from caerp.views import BaseRestView, RestListMixinClass
from caerp.views.status.rest_api import StatusLogEntryRestView
from caerp.views.status.utils import get_visibility_options

from caerp.views.files.rest_api import FileRestView

from .routes import (
    API_ROUTE,
    API_ROUTE_GEOJSON,
    API_ITEM_ROUTE,
    API_LOGO_ROUTE,
    API_LOGO_ITEM_ROUTE,
    API_HEADER_ROUTE,
    API_HEADER_ITEM_ROUTE,
)
from .views import get_enabled_bookeeping_modules


logger = logging.getLogger(__name__)


class CompanyMapSearchTools:
    """
    Filters and schema for map search.
    Sur la même logique que UserFilterTools
    """

    list_schema = get_mapsearch_schema()

    def filter_search(self, query, appstruct):
        search = appstruct.get("search")
        if search:
            query = query.filter(
                or_(
                    Company.name.like("%" + search + "%"),
                    Company.goal.like("%" + search + "%"),
                    Company.employees.any(User.lastname.like("%" + search + "%")),
                    Company.employees.any(User.firstname.like("%" + search + "%")),
                    Company.employees.any(
                        User.login.has(Login.login.like("%" + search + "%"))
                    ),
                ),
            )
        return query

    def filter_activity_id(self, query, appstruct):
        activity_id = appstruct.get("activity_id")
        if activity_id:
            query = query.filter(
                Company.activities.any(CompanyActivity.id == activity_id)
            )
        return query

    def filter_postcode(self, query, appstruct):
        postcode = appstruct.get("postcode")
        if postcode:
            query = query.filter(Company.zip_code == postcode)
        return query


class CompanyRestListMixin(
    CompanyMapSearchTools,
    RestListMixinClass,
):
    """
    Rest list logic for Company
    """

    # list_schema defined in the filter class
    authorized_fields = {
        "id",
        "name",
        "goal",
        "email",
        "mobile",
        "phone",
        "zip_code",
        "latitude",
        "longitude",
        "users_gallery",
        "activities_labels",
    }

    def query(self):
        query = Company.query()
        fields = self.collection_fields()
        if fields:
            logger.info("Returning only {}".format(fields))
            mapper_fields = set(self._mapper_fields()).intersection(fields)
            query = query.options(load_only(*mapper_fields))
        return query

    def format_collection(self, query):
        fields = self.collection_fields()
        return [
            dict((field, getattr(company, field)) for field in fields)
            for company in query
        ]

    def collection_fields(self):
        fields = set(self.request.params.getall("fields"))

        # Only authorize public informations for non-admins
        if not self.request.has_permission(PERMISSIONS["global.company_view"]):
            fields = fields.intersection(self.authorized_fields)
        if not fields:
            fields = ["id", "name"]
        return fields

    @staticmethod
    def _mapper_fields() -> Iterable[str]:
        """
        Returns mapped column names available on a Company
        :return:
        """
        mapper = inspect(Company)
        return (i.key for i in mapper.attrs)


<<<<<<< Updated upstream
=======
class PaginationSchema(colander.MappingSchema):
    page = colander.SchemaNode(
        colander.Integer(),
        default=0,
        missing=0,
        validator=colander.Range(min=0),
        title="Numéro de page",
    )
    per_page = colander.SchemaNode(
        colander.Integer(),
        default=50,
        missing=50,
        validator=colander.Range(min=1, max=1000000),
    )


class SortSchema(colander.MappingSchema):
    sort = colander.SchemaNode(
        colander.String(),
        title="Colonne de tri",
    )
    sort_direction = colander.SchemaNode(
        colander.String(),
        title="Ordre de tri",
        default="asc",
        missing="asc",
        validator=colander.OneOf(["asc", "desc"]),
    )


class FilterSchema(colander.MappingSchema):
    search = colander.SchemaNode(
        colander.String(),
        title="Recherche",
    )


class CompanyFilterSchema(FilterSchema):
    activity_id = colander.SchemaNode(
        colander.Integer(),
        title="Activité",
    )


class BaseSerializer:
    acl = None
    # Used to avoid circular serialization issues
    exclude_from_children = None

    def __init__(self, fields: dict, serializer_registry: dict, excludes: Tuple = ()):
        self.fields = fields
        self.attributes = fields.get("attributes", [])
        self.relationships = fields.get("relationships", {})
        self.serializer_registry = serializer_registry
        self.excludes = excludes
        self.load_relationships_serializer(serializer_registry)
        if self.acl is None:
            raise Exception(f"No ACL defined for serializer {self.__class__.__name__}")
        elif self.exclude_from_children is None:
            raise Exception(
                f"No exclude_from_children defined for serializer {self.__class__.__name__}"
            )

    def non_plural_relationship_name(self, relation_name: str) -> str:
        if relation_name.endswith("s"):
            return relation_name[:-1]
        return relation_name

    def load_relationships_serializer(self, serializer_registry: dict) -> dict:
        self.relationships_serializer = {}
        for relation_name, relation_fields in self.relationships.items():
            relationship_name = self.non_plural_relationship_name(relation_name)
            serializer = serializer_registry.get(relationship_name)

            if serializer is not None:
                self.relationships_serializer[relation_name] = serializer(
                    relation_fields,
                    serializer_registry,
                    # On évite les récursions
                    excludes=self.exclude_from_children,
                )

    def is_attribute_allowed(self, request, item, attribute: str) -> bool:
        """
        Check if a field is allowed in export
        """
        global_acl = self.acl.get("__all__")
        if global_acl is not None and request.has_permission(global_acl, item):
            return True
        else:
            acl = self.acl.get(attribute)
            if acl is not None and request.has_permission(acl, item):
                return True
        return False

    def is_relationship_allowed(self, request, item, relationship_name: str) -> bool:
        if relationship_name in self.excludes:
            return False

        acl = self.acl.get(relationship_name)

        if acl is not None:
            return request.has_permission(acl, item)
        return False

    def run(self, request, item) -> dict:
        result = {}
        for field in self.attributes:
            if field in self.excludes or not self.is_attribute_allowed(
                request, item, field
            ):
                continue
            db_value = getattr(item, field)
            formatter = getattr(self, f"format_{field}", None)
            if formatter is not None:
                value = formatter(db_value)
            else:
                value = db_value
            result[field] = value

        for relation_name in self.relationships:
            if relation_name in self.excludes or not self.is_relationship_allowed(
                request, item, relation_name
            ):
                continue
            serializer = self.relationships_serializer.get(relation_name)
            db_value = getattr(item, relation_name, None)
            if serializer is not None:
                if isinstance(db_value, (list, set, tuple)):
                    result[relation_name] = [
                        serializer.run(request, item) for item in db_value
                    ]
                else:
                    result[relation_name] = serializer.run(request, db_value)
            else:
                result[field] = db_value
        return result


class CompanySerializer(BaseSerializer):
    acl = {
        "id": PERMISSIONS["global.authenticated"],
        "name": PERMISSIONS["global.authenticated"],
        "goal": PERMISSIONS["global.authenticated"],
        "email": PERMISSIONS["global.authenticated"],
        "mobile": PERMISSIONS["global.authenticated"],
        "phone": PERMISSIONS["global.authenticated"],
        "zip_code": PERMISSIONS["global.authenticated"],
        "latitude": PERMISSIONS["global.authenticated"],
        "longitude": PERMISSIONS["global.authenticated"],
        "users_gallery": PERMISSIONS["global.authenticated"],
        "activities_labels": PERMISSIONS["global.authenticated"],
        "__all__": PERMISSIONS["global.company_view"],
        "customers": PERMISSIONS["global.company_view"],
        "suppliers": PERMISSIONS["global.company_view"],
        "tasks": PERMISSIONS["global.company_view"],
        "invoices": PERMISSIONS["global.company_view"],
        "estimations": PERMISSIONS["global.company_view"],
        "supplier_invoices": PERMISSIONS["global.company_view"],
        "supplier_orders": PERMISSIONS["global.company_view"],
        "projects": PERMISSIONS["global.company_view"],
        "businesses": PERMISSIONS["global.company_view"],
        "employees": PERMISSIONS["global.company_view"],
    }

    exclude_from_children = (
        "company",
        "companies",
    )


class CustomerSerializer(BaseSerializer):
    acl = {
        "id": PERMISSIONS["global.company_view"],
        "name": PERMISSIONS["global.company_view"],
        "label": PERMISSIONS["global.company_view"],
    }
    exclude_from_children = ("customer", "customers")


serializers = {"company": CompanySerializer, "customer": CustomerSerializer}


class CompanyRestListViewV2(BaseRestView):
    """

    GET ?filter_antenne_id=num&filter_follower_id=num&filter_activity_id=num&sort.sort=lastname&sort.sortDirection=desc&pagination.page=1&pagination.per_page=10


    En entrée :

    - LoadOptions

    En retour

    - RestCollectionResponse
    """

    def validate_pagination_options(self, load_options: LoadOptions):
        pagination_schema = PaginationSchema()
        try:
            return pagination_schema.deserialize(load_options.pagination)
        except colander.Invalid as e:
            raise RestError(str(e))

    def validate_sort_options(self, load_options: LoadOptions):
        sort_schema = SortSchema()
        try:
            return sort_schema.deserialize(load_options.sort)
        except colander.Invalid as e:
            raise RestError(str(e))

    def validate_filters(self, load_options: LoadOptions):
        filter_schema = CompanyFilterSchema()
        try:
            return filter_schema.deserialize(load_options.filters)
        except colander.Invalid as e:
            raise RestError(str(e))

    def validate_fields(self, load_options: LoadOptions):
        # TODO
        return load_options.fields

    def build_main_query(self, filters: Optional[dict], fields: Optional[dict]):
        query = Company.query()
        if fields:
            attributes = []
            for field in fields:
                if fields[field] == {}:
                    attributes.append(getattr(Company, field))
            if attributes:
                query = query.options(load_only(attributes))
        return query

    def sort_query(self, query, sort: SortOptions):
        if sort.sort:
            if sort.sort_direction == "asc":
                func = asc
            else:
                func = desc
            query = query.order_by(func(getattr(Company, sort.sort)))
        return query

    def paginate_query(self, query, pagination: PaginationOptions):
        page = pagination.page
        per_page = pagination.per_page
        return query.offset(page * per_page).limit(per_page)

    def _format_result_items(self, query, fields):
        result = []
        for db_item in self.request.dbsession.execute(query).scalars():
            item_dict = {}
            for attribute in fields:
                db_value = getattr(db_item, attribute)
                formatter = getattr(self, f"format_{attribute}_item", None)
                if formatter is None:
                    item_dict[attribute] = db_value
                else:
                    item_dict[attribute] = formatter(db_value)
            result.append(item_dict)
        return result

    def build_collection_response(
        self, query, fields, pagination, query_count
    ) -> RestCollectionResponse:
        items = self._format_result_items(query, fields)
        metadata = RestCollectionMetadata(
            page=pagination.page,
            items_per_page=pagination.per_page,
            total_count=query_count,
        )
        return RestCollectionResponse(
            items=items,
            metadata=metadata,
        )

    def collection_get(self) -> RestCollectionResponse:
        load_options = LoadOptions.from_request(self.request)
        pagination: PaginationOptions = self.validate_pagination_options(load_options)
        sort: SortOptions = self.validate_sort_options(load_options)
        filters = self.validate_filters(load_options)
        fields = self.validate_fields(load_options)

        query = self.build_main_query(filters, fields)
        query_count = self.request.dbsession.execute(query.count()).scalar_one()
        query = self.sort_query(query, sort)
        query = self.paginate_query(query, pagination)
        results = self.build_collection_response(query, fields, pagination, query_count)
        return results

    def get_list_schema(self):
        return get_list_schema().bind(request=self.request)

    def form_config(self):
        return {
            "schema": convert_to_jsonschema(self.get_list_schema()),
        }

    def __call__(self, request):
        logger.debug("Received parameters")
        logger.debug(LoadOptions.from_request(self.request))
        return {}


>>>>>>> Stashed changes
class CompanyRestView(
    CompanyRestListMixin,
    BaseRestView,
):
    """
    Rest Class for company
    """

    def get_schema(self, submitted: Optional[dict] = None) -> colander.Schema:
        is_accountant = bool(
            self.request.has_permission(PERMISSIONS["global.manage_accounting"])
        )
        is_company_admin = bool(
            self.request.has_permission(PERMISSIONS["global.create_company"])
        )
        is_company_supervisor = bool(
            self.request.has_permission(PERMISSIONS["global.company_view"])
        )
        modules = get_enabled_bookeeping_modules()
        excludes = [key for key, value in modules.items() if not value]

        return get_company_schema(
            is_accountant=is_accountant,
            is_company_admin=is_company_admin,
            is_company_supervisor=is_company_supervisor,
            excludes=excludes,
        )

    def pre_format(self, datas, edit=False):
        result = super().pre_format(datas, edit)

        # Exit la modification du nom pour les personnes n'ayant pas le rôle
        # global.create_company
        if (
            edit
            and "name" in result
            and not self.request.has_permission("global.create_company")
        ):
            result.pop("name")
        return result

    def after_flush(self, company, edit, appstruct):
        user_id = appstruct.pop("user_id", None)
        if user_id is not None:
            user_account = User.get(user_id)
            if user_account is not None:
                company.employees.append(user_account)
                company.set_datas_from_user(user_account)
        return company

    def format_item_result(self, model) -> Union[dict, object]:
        out = super().format_item_result(model)
        if isinstance(out, DBBASE):
            out = out.__json__(self.request)
        if "activities" in out:
            # De-hydrate property
            out["activities"] = [i.id for i in out["activities"]]

        return out

    @staticmethod
    def _get_decimal_to_display_options() -> List[Dict]:
        return [{"id": id, "label": label} for id, label in DECIMAL_TO_DISPLAY_VALUES]

    @staticmethod
    def _get_antennes_options():
        return [{"id": id, "label": label} for id, label in get_antenne_options()]

    @staticmethod
    def _get_follower_options():
        return [
            {"id": id, "label": label}
            for id, label in get_users_options(
                account_type=ACCOUNT_TYPES["equipe_appui"]
            )
        ]

    @staticmethod
    def _get_deposit_options():
        return [{"id": value, "label": f"{value} %"} for value in range(0, 90, 10)]

    def form_config(self):
        if isinstance(self.context, Company):
            company_id = self.context.id
        else:
            company_id = None

        return {
            "options": {
                "company_id": company_id,
                "visibilities": get_visibility_options(self.request),
                "activities": self.get_activities_options(),
                "decimal_to_display": self._get_decimal_to_display_options(),
                "antennes_options": self._get_antennes_options(),
                "follower_options": self._get_follower_options(),
                "deposit_options": self._get_deposit_options(),
            },
            "schemas": {"default": convert_to_jsonschema(self.get_schema())},
        }

    @staticmethod
    def get_activities_options():
        return [
            {"id": c.id, "label": c.label}
            for c in CompanyActivity.query("id", "label").all()
        ]


class CompanyRestGeoJSONView(CompanyRestView):
    """
    Get companies in GeoJSON format
    """

    def collection_fields(self):
        fields = super().collection_fields()
        fields.add("latitude")
        fields.add("longitude")
        return fields

    def query(self):
        query = super().query()
        query = query.filter(Company.latitude.isnot(None))
        query = query.filter(Company.longitude.isnot(None))
        return query

    def company_to_geojson_feature(self, company: Company):
        fields = self.collection_fields()
        db_fields = [
            i
            for i in fields
            if i not in ("users_gallery", "latitude", "longitude", "activities_labels")
        ]
        properties = {key: getattr(company, key) for key in db_fields}
        if "users_gallery" in fields:
            properties["users_gallery"] = [
                dict(
                    fullname=f"{user.firstname} {user.lastname}",
                    logo_url=(
                        f"/files/{user.photo_id}?action=download"
                        if user.photo_id and user.photo_is_publishable
                        else None
                    ),
                )
                for user in company.employees
            ]
        if "activities_labels" in fields:
            properties["activities_labels"] = [i.label for i in company.activities]

        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [company.longitude, company.latitude],
            },
            "properties": properties,
        }

    def format_collection(self, query):
        features = [self.company_to_geojson_feature(company) for company in query]
        geojson = {"type": "FeatureCollection", "features": features}

        return geojson


class CompanyLogoSchema(FileUploadSchema):
    filters = [
        ImageResizer(800, 800),
    ]
    upload = ImageNode(preparer=get_file_upload_preparer(filters))
    parent_id = colander.SchemaNode(
        colander.Integer(),
        missing=colander.drop,
        widget=deform.widget.HiddenWidget(),
        validator=deferred_parent_id_validator,
    )


class CompanyLogoRestView(FileRestView):
    def get_schema(self, submitted: Optional[dict] = None):
        return CompanyLogoSchema()


class CompanyHeaderSchema(colander.Schema):
    filters = [
        ImageRatio(4, 1),
        ImageResizer(2000, 500),
    ]
    upload = ImageNode(preparer=get_file_upload_preparer(filters))
    parent_id = colander.SchemaNode(
        colander.Integer(),
        missing=colander.drop,
        widget=deform.widget.HiddenWidget(),
        validator=deferred_parent_id_validator,
    )


class CompanyHeaderRestView(FileRestView):
    def get_schema(self, submitted: Dict):
        return CompanyHeaderSchema()


def includeme(config):
    config.add_rest_service(
        factory=CompanyRestView,
        route_name=API_ITEM_ROUTE,
        collection_route_name=API_ROUTE,
        view_rights=PERMISSIONS["company.view"],
        add_rights=PERMISSIONS["global.create_company"],
        edit_rights=PERMISSIONS["context.edit_company"],
        collection_view_rights=PERMISSIONS["global.authenticated"],
        context=Company,
    )

    for route_name, context, permission in (
        (API_ROUTE, None, "global.create_company"),
        # company.view et pas edit car utilisé pour les mémos
        (API_ITEM_ROUTE, Company, "company.view"),
    ):
        # form_config for both add and edit
        config.add_view(
            CompanyRestView,
            attr="form_config",
            route_name=route_name,
            renderer="json",
            request_param="form_config",
            permission=PERMISSIONS[permission],
            context=context,
        )

    config.add_rest_service(
        factory=CompanyRestGeoJSONView,
        collection_route_name=API_ROUTE_GEOJSON,
        collection_view_rights=PERMISSIONS["global.authenticated"],
    )

    config.add_view(
        CompanyRestGeoJSONView,
        attr="form_config",
        route_name=API_ROUTE_GEOJSON,
        renderer="json",
        request_param="form_config",
        permission=PERMISSIONS["global.authenticated"],
    )

    config.add_rest_service(
        StatusLogEntryRestView,
        "/api/v1/companies/{eid}/statuslogentries/{id}",
        collection_route_name="/api/v1/companies/{id}/statuslogentries",
        collection_view_rights=PERMISSIONS["company.view"],
        add_rights=PERMISSIONS["company.view"],
        view_rights=PERMISSIONS["context.view_statuslogentry"],
        edit_rights=PERMISSIONS["context.edit_statuslogentry"],
        delete_rights=PERMISSIONS["context.delete_statuslogentry"],
    )

    config.add_view(
        CompanyLogoRestView,
        request_method="POST",
        attr="post",
        route_name=API_LOGO_ROUTE,
        permission=PERMISSIONS["global.authenticated"],
        require_csrf=True,
        renderer="json",
    )

    config.add_rest_service(
        CompanyLogoRestView,
        route_name=API_LOGO_ITEM_ROUTE,
        view_rights=PERMISSIONS["context.view_file"],
        edit_rights=PERMISSIONS["context.edit_file"],
        delete_rights=PERMISSIONS["context.delete_file"],
        context=File,
    )

    config.add_view(
        CompanyHeaderRestView,
        request_method="POST",
        attr="post",
        route_name=API_HEADER_ROUTE,
        permission=PERMISSIONS["global.authenticated"],
        require_csrf=True,
        renderer="json",
    )

    config.add_rest_service(
        CompanyHeaderRestView,
        route_name=API_HEADER_ITEM_ROUTE,
        view_rights=PERMISSIONS["context.view_file"],
        edit_rights=PERMISSIONS["context.edit_file"],
        delete_rights=PERMISSIONS["context.delete_file"],
        context=File,
    )
