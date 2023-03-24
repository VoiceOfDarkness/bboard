from django.contrib import admin

from .forms import SubRubricForm
from .models import SubRubric, SuperRubric


class SubRubricInlince(admin.TabularInline):
    model = SubRubric


@admin.register(SuperRubric)
class SuperRubricAdmin(admin.ModelAdmin):
    model = SuperRubric
    exclude = ('super_rubric',)
    inlines = (SubRubricInlince,)
    

@admin.register(SubRubric)
class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm
