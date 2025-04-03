import os
from mopidy import config, ext
from .http import factory_decorator
from .actor import Frontend

__version__ = '0.9.15'


class Extension(ext.Extension):
    dist_name = 'Mopidy-SevenSegmentDisplay'
    ext_name = 'sevensegmentdisplay'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['display_enabled'] = config.Boolean()
        schema['buttons_enabled'] = config.Boolean()
        schema['light_sensor_enabled'] = config.Boolean()
        schema['relay_enabled'] = config.Boolean()
        schema['ir_remote'] = config.String()
        schema['default_tracks'] = config.String()
        schema['default_volume'] = config.Integer()
        schema['default_preset'] = config.String()
        schema['alert_files'] = config.String(optional=True)
        schema['display_min_brightness'] = config.Integer()
        schema['display_max_brightness'] = config.Integer()
        schema['equalizer_enabled'] = config.Boolean()
        schema['mqtt_host'] = config.String()
        schema['mqtt_port'] = config.String()
        schema['mqtt_user'] = config.String()
        schema['mqtt_password'] = config.String()
        return schema

    def setup(self, registry):
        registry.add('frontend', Frontend)
        registry.add('http:app', {
            'name': self.ext_name,
            'factory': factory_decorator(Frontend.worker),
        })
