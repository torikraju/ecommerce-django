from django.views.generic import ListView

from app_dir.products.models import Product


class SearchView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        """
            __icontains = field contains this
            __iexact = fields is exactly this
        """
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)  # method_dict['q']
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return None
