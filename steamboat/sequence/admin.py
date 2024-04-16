from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Platform, Selection, Sequence, Source, Strategy


@admin.register(Sequence)
class SequenceAdmin(ModelAdmin):
    pass


@admin.register(Platform)
class PlatformAdmin(ModelAdmin):
    search_fields = [
        "platform__name",
        "platform__model",
    ]
    list_display = ["name", "model"]
    ordering = ["name", "model"]


@admin.register(Strategy)
class StrategyAdmin(ModelAdmin):
    search_fields = [
        "strategy__name",
        "strategy__description",
    ]
    list_display = ["name", "description"]
    ordering = ["name"]


@admin.register(Source)
class SourceAdmin(ModelAdmin):
    search_fields = [
        "source__name",
        "source__description",
    ]
    list_display = ["name", "description"]
    ordering = ["name"]


@admin.register(Selection)
class SelectionAdmin(ModelAdmin):
    search_fields = [
        "selection__name",
        "selection__description",
    ]
    list_display = ["name", "description"]
    ordering = ["name"]
