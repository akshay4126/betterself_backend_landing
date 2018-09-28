PROGRAMS = (
    {
        'command': 'celery worker -A betterself_backend -Q betterself_main -n betterself_main -l INFO',
        'name': 'betterself_main'
    },
)
