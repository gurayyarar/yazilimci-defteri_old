from docutils import nodes
from docutils.nodes import Body, Element
from docutils.parsers.rst import Directive


class disqus(Body, Element):
    pass


class Disqus(Directive):
    def run(self):
        node = disqus()
        return [node]


def html_disqus(self, node):
    template = """
        <hr />
        <div id="disqus_thread"></div>
        <script>
            (function() { // DON'T EDIT BELOW THIS LINE
                var d = document, s = d.createElement('script');
                s.src = 'https://yazilimcidefteri.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    """

    self.body.append(template)
    raise nodes.SkipNode


def setup(app):
    app.add_node(disqus, html=(html_disqus, None))
    app.add_directive("disqus", Disqus)
