from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
import csv
import datetime
from django.core.urlresolvers import reverse
from django.utils.html import format_html


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):

    def OrderDetail(obj):
        return format_html('<a href="{}">Посмотреть</a>'.format(
            reverse('orders:AdminOrderDetail', args=[obj.id])
        ))

    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', OrderDetail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    def ExportToCSV(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; \
            filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
        writer = csv.writer(response)

        fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
        # Первая строка- оглавления
        writer.writerow([field.verbose_name for field in fields])
        # Заполняем информацией
        for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)
            writer.writerow(data_row)
        return response

        ExportToCSV.short_description = 'Export CSV'



    actions = [ExportToCSV] # Добалено при улучшении админки, для выгрузки CSV


admin.site.register(Order, OrderAdmin)



