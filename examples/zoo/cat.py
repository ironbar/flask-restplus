from flask_restplus import Namespace, Resource, fields

api = Namespace('cats', description='Cats related operations')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]


class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS


@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)

class CatBackend(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.backend = kwargs['backend']

    @api.doc('Returns backend result')
    def get(self):
        '''Returns backend result'''
        return self.backend.get()

def register_resources(backend):
    global api
    api.add_resource(CatList, '')
    api.add_resource(Cat, '<id>')
    api.add_resource(CatBackend, 'backend', resource_class_kwargs=dict(backend=backend))
