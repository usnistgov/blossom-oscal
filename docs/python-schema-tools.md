## XSD/JSONSchema Tooling Packages for Python

1. XSD->Python [info source 1](https://stackoverflow.com/questions/1072853/how-to-convert-xsd-to-python-class)
   1. Pip-installable [xmlschema](https://xmlschema.readthedocs.io/en/latest/usage.html)
       - The project has support of EU project MaX ([**Ma**terials design at the e**X**ascale](http://www.max-centre.eu/)). MaX project is on official [EU Registry](https://cordis.europa.eu/project/id/824143) and one can learn about it in the [video](http://www.max-centre.eu/).
       - 
   2. [generateDS](https://www.davekuhlman.org/generateDS.html) project is in two repositories [gitlab](https://gitlab.com/cdehealth/generateds/-/tree/main) 
       - Written and supported predominantly by a single developer - [Dave Kuhlman](http://www.davekuhlman.org/)
       - [+] Has a one-page [usage guide](https://www.davekuhlman.org/generateDS.html)
       - [+] Has an accompanying CLI tool to generate XSD mapping to Python classes
   3. PyXB - originally was intended to be JaXB equivalent
      - Works with very limited XSD versions
      - Reached the End-of-Life, but still can be used
      - [GitHub Repo](https://github.com/pabigot/pyxb) is stale since 2018-02-11
      - Has an [extended fork PyXB-X](https://github.com/renalreg/PyXB-X) for projects with dependent pipelines and if pip-deployable
  