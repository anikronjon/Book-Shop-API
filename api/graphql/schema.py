import graphene
from graphene_django import DjangoObjectType,DjangoListField
from api.models import Category, Post, Comment


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"


class Query(graphene.ObjectType):
    categories = DjangoListField(CategoryType)
    posts = DjangoListField(PostType)
    comments = DjangoListField(CommentType)


