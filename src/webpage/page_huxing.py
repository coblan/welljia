from .page_home import Home
from .models import Building

class Huxing(Home):
    def get_template(self): 
        return 'webpage/huxing.html'
    def extraCtx(self):
        builds = []
        for build in Building.objects.order_by('order'):
            builds.append({
                'label': build.label,
                'floors': [
                    {'label': x.label, 'status': x.status, 'img_2d': x.floortype.img_2d, 'img_3d': x.floortype.img_3d,} 
                    for x in build.floor_set.order_by('order')
                    ],
            })
        
        return {
            'crt_page_name':'huxing',
            'builds': builds,
        }    