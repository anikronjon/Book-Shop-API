from api.forms import CategoryForm, PostForm, CommentForm
from .schema import CategoryType, PostType, CommentType
import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation


class CategoryMutation(DjangoModelFormMutation):
    category = graphene.Field(CategoryType)

    class Meta:
        form_class = CategoryForm


class PostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)

    class Meta:
        form_class = PostForm


class CommentMutation(DjangoModelFormMutation):
    comment = graphene.Field(CommentType)

    class Meta:
        form_class = CategoryForm


class Mutation(graphene.ObjectType):
    category = CategoryMutation.Field()
    post = PostMutation.Field()
    comment = CommentMutation.Field()



