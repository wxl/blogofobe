`blogofobe` is an attempt to keep [Blogofile](http://blogofile.com/) going. At the time this was forked from it, there were plenty of issues that weren't getting replied to and pull requests that weren't getting merged. I tried to write the authors but didn't get much in turn. As a user of Blogofile, I wanted to keep it going.

Oh, and about the name. Blogofile is a play on the notion of a blog addict ("blogophile") and the fact that everything's a file rather than having some silly CMS. I like this notion, but the thing that has kept me from blogging in the past is that they all had some ridiculously bloated web interface and/or that I had to touch HTML or CSS. I understand it, but I don't like it. Not when it comes to writing, at least. So I consider myself a blogophobe. I'm afraid of typical blogs. `blogofobe` is a soothing balm to CLI users like myself.

If there's any weird stuff that seems to be holdovers from Blogofile, it probably is. Pull requests welcome!

===

Blogofobe is a static website compiler that lets you use various template
libraries (Mako, Jinja2),
and various markup languages (reStructuredText, Markdown, Textile)
to create sites that can be served from any web server you like.

`blogofobe_blog` is a blog engine plugin. With it installed you get a simple blog engine that requires no
database and no special hosting environment.
You customize a set of Mako templates,
create posts in reStructuredText, Markdown, or Textile, (or even plain HTML)
and blogofobe generates your entire blog as
plain HTML, CSS, images, and Atom/RSS feeds
which you can then upload to any old web server you like.
No CGI or scripting environment is needed on the server.

See the [Blogofile website](http://blogofile.com/) for an example of a Blogofobe-generated
site that includes a blog,
and check out the [project docs](http://blogofile.readthedocs.org/en/latest/
) for a quick-start guide,
and detailed usage instructions.

Or, if you're the "just get it done sort",
create a virtualenv,
and dive in with::

    pip install -U Blogofile
    pip install -U blogofile_blog
