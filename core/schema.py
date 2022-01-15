import graphene
import api.graphql.schema


class Query(api.graphql.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
