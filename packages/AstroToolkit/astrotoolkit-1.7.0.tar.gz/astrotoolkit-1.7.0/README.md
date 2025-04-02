AstroToolkit
============

AstroToolkit (ATK) is a set of tools for fetching, plotting, and analysing astronomical data.

<br>

Features
--------

* A GUI through which most of the package can be utilised
* Command-line integration
* Proper motion correction through Gaia, utilised across the entire package
* Light curve, spectral energy distribution, spectrum and image queries from a wide range of surveys
* Gaia HRD queries for any Gaia sources
* In-built interactive plotting support for all of the above as shareable .html pages that retain all interactivity
* Data queries from any [Vizier](https://vizier.cds.unistra.fr/) survey, with many commonly used surveys built-in
* Reddening queries from [Stilism](https://stilism.obspm.fr/) and [GDRE](https://irsa.ipac.caltech.edu/applications/DUST/)
* Data analysis tools: 
    * Timeseries analysis
    * Light curve binning, clipping, phase folding and sigma-clipping
    * Image detection and tracer overlays
    * Spectral band highlighting
    * SED-spectrum overlays
    * Data quality filtering (optional)
* Lossless saving and reading of any ATK data structures to / from local files
* Datapage creation, allowing the combination of any of the above into a single page with additional elements specifically designed for this purpose
* No hard coded parameters - built-in configuration support allows the user to personalise the package to their specific needs.
* All data structures are available to the user, allowing them to use all ATK routines on non-ATK data
* Other quality-of-life tools, such as coordinate conversions, .fits file reading and [Vizier](https://vizier.cds.unistra.fr/) / [SIMBAD](https://simbad.u-strasbg.fr/simbad/) searches

<br>

Acknowledgements
----------------
This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (Grant agreement No. 101020057).

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./docs/images/erc_logo_dark.png">
        <source media="(prefers-color-scheme: light)" srcset="./docs/images/erc_logo_light.png">
        <img src="./images/erc_logo_dark.png" width="200"/>
    </picture>
</p>

<br>

I would like to give thanks to Dr. Keith Inight for his guidance at various stages of the package's development.

I would also like to give thanks to Prof. Boris Gänsicke for his assistance and guidance, and for supporting the package's development.

<br>

Documentation
-------------

Full documentation for the package can be found [here](https://astrotoolkit.readthedocs.io/en/latest/).
