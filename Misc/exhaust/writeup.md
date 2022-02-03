> # Exhaust
> > Misc - 200 pts

> A brave team of engineers from the Distributed Interstellar Patient System (DIPS) have recovered a secret file which could point to a vulnerability in the Empire's defenses.

> Sadly, the engineers are missing a key piece of equipment to find this vulnerability - can you help?

> Hint 1: Replicators neither exist in Star Wars nor in real life... but do you have something close to one? What's a "facet normal" anyway?

> Hint 2: You might need to make a trench run of your own - your ship will need to be a real *slicer* or a *blender*...

> Hint 3: If it's tricky to spot the vulnerability, look for the "wireframe" or "X-ray" switch...

## Writeup


The file is an .STL model in ASCII format. Loading it into Blender or a slicer (such as Ultimaker Cura) will show it's a model of the Death Star. Turning on wireframe mode (Z -> 4) in Blender or "X-ray mode" in the slicer will reveal a secret trench, containing the solution.

```UiTHack22{pick-up-your-3d-visuals}```

Credit to Elproducts (https://www.thingiverse.com/thing:1158483) for the base model.