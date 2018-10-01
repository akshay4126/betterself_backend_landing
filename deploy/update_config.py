import os
from optparse import OptionParser
from jinja2 import Environment, FileSystemLoader

# noinspection PyUnresolvedReferences
from celery_programs import PROGRAMS

PRODUCTION_BRANCH = 'master'
parser = OptionParser()
conf_choices = ('nginx', 'celery')
parser.add_option('--conf', action='store', dest='conf', choices=conf_choices,
                  help=f'Config name. Valid choices are: {str(conf_choices)}.')
parser.add_option('--host', action='store', type='string', dest='host',
                  help='Host (nginx server_name).')
parser.add_option('--branch', action='store', type='string', dest='branch',
                  help='Git branch.')

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'confs')
env = Environment(loader=FileSystemLoader(path))


def update_nginx_conf(host, branch):
    nginx_conf_path = '/etc/nginx/sites-enabled/'
    template_name = 'betterself_nginx.prod.conf.tpl' if branch == PRODUCTION_BRANCH else 'betterself_nginx.conf.tpl'
    template = env.get_template(template_name)
    conf = template.render(host=host)
    with open(os.path.join(nginx_conf_path, 'betterself_nginx.conf'), 'w') as f:
        f.write(conf)


def update_celery_conf():
    celery_conf_path = '/etc/supervisor/conf.d/'
    template = env.get_template('betterself_celery.conf.tpl')
    programs = []
    for program in PROGRAMS:
        programs.append(template.render(**program))
    with open(os.path.join(celery_conf_path, 'betterself_celery.conf'), 'w') as f:
        f.write('\n\n'.join(programs))


def main():
    options, args = parser.parse_args()
    assert options.conf, '--conf option is required.'
    if options.conf == 'nginx':
        assert options.host, '--host option is required.'
        assert options.branch, '--branch option is required.'
        update_nginx_conf(options.host, options.branch)
    elif options.conf == 'celery':
        update_celery_conf()


if __name__ == '__main__':
    main()
