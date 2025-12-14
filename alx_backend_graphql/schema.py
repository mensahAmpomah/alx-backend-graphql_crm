import graphene


class CRMQuery:
    """
    Base query class for CRM-related queries.
    (Can be extended later)
    """
    pass


class Query(CRMQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")


schema = graphene.Schema(query=Query)