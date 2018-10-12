from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['', 'about']

    def location(self, item):
        return f'/{item}'
