# Pipe pipe_926a27580e74684fc63559b92bddaa30 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipeuniq import pipe_uniq
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.pipesort import pipe_sort
from pipe2py.modules.pipeoutput import pipe_output


def pipe_926a27580e74684fc63559b92bddaa30(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    forever = pipe_forever()

    sw_68 = pipe_fetch(
        context, forever, conf={'URL': [{'type': 'url', 'value': 'http://www.guru.com/rss/jobs/c/web-software-it/'}, {'type': 'url', 'value': 'https://www.elance.com/r/rss/jobs/cat-it-programming/fxd-true/o-1/bgt-gt500-ns1/sct-database-development-10217-data-analysis-14174-database-administration-14177-business-intelligence-14173-data-engineering-14175-system-administration-10219-other-data-science-14178-technical-support-10218-other-it-programming-12350-software-application-10216-website-design-10225-web-programming-10224/tls-1/s-timelistedSort'}]})
    
    sw_90 = pipe_uniq(
        context, sw_68, conf={'field': {'type': 'text', 'value': 'link'}})
    
    sw_87 = pipe_filter(
        context, sw_90, conf={'COMBINE': {'type': 'text', 'value': 'or'}, 'MODE': {'type': 'text', 'value': 'block'}, 'RULE': [{'field': {'type': 'text', 'value': 'title'}, 'value': {'type': 'text', 'value': 'php'}, 'op': {'type': 'text', 'value': 'contains'}}]})
    
    sw_101 = pipe_sort(
        context, sw_87, conf={'KEY': [{'field': {'type': 'text', 'value': 'pubDate'}, 'dir': {'type': 'text', 'value': 'DESC'}}]})
    
    _OUTPUT = pipe_output(
        context, sw_101, conf={})
    
    return _OUTPUT


if __name__ == "__main__":
    context = Context()
    pipeline = pipe_926a27580e74684fc63559b92bddaa30(context, None)

    for i in pipeline:
        print i