# Mii

Core Mii implementation in [Fusion](https://fusion-lang.org/).

So far, the only thing written is `FFLResource`, which should allow you to load `FFLRes*.dat` files. Soon enough, I will provide examples (e.g. a three.js renderer of shapes) to show that this works.

## TODOs

#### Core

* [ ] `FFLResource` full implementation (textures & shapes)
* [X] `Ver3StoreData` (from Arian's repo)
* [ ] `Expression`
* [ ] FFLDatabase

#### API-Specific

* [ ] An FFL render server (like [mii-unsecure](https://mii-unsecure.ariankordi.net/))
* [ ] Implement in [GDFL](https://github.com/GloriousGlider8/GDFL) (GoDot Face Library)
* [ ] three.js impl.

#### Extras

* [ ] Extended file format support (`rsd`, `charinfo` and maybe even  `miic`..?)
* [ ] Custom Expression support..?
* [ ] Data Conversions
