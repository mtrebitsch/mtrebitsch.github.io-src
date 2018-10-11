Research
########

Understanding the sources of reionisation
-----------------------------------------

The goal of my current research is to understand the properties of the galaxies responsible for the reionisation of the universe.

The Epoch of Reionsation
""""""""""""""""""""""""

.. figure:: {filename}/img/reion_diagram.jpg
   :alt: The Epoch of Reionisation in the universe timeline
   :align: left
   :figwidth: 40%
   :width: 95%

Shortly after the Big Bang, the gas in the universe was cool enough for electrons and protons to form hydrogen and helium atoms, and all the gas became neutral.

When the first radiative sources (most likely the first stars and galaxies) started to form, around *z* ~ 15 -- 20, the energetic radiation emitted by those sources started to ionise the neutral hydrogen around them, carving ionised bubbles in the intergalactic medium (IGM). As the primeval galaxies grow and assemble their stars, these ionised regions will grow and overlap, eventually filling the whole universe around *z* ~ 6. This transition epoch is called the *Epoch of Reionisation* (EoR).

.. say something about the observational evidences

Studying this phase transition is crucial to investigate the history of the universe, and this require to understand the formation of the first objects. These high-*z* objects are very difficult to observe with the current generation of telescopes, but the upcoming James Webb Space Telescope (JWST) and the Square Kilometer Array (SKA) are promising future instruments thare are going to see these first galaxies and the distribution of neutral gas around them.

The reionisation process
~~~~~~~~~~~~~~~~~~~~~~~~

There are several issues that need to be addressed in order to shed some light on the detailed history of reionisation, with perhaps the most important being: what are the ionising sources? While the current scenario favours the idea that galaxies are responsible for the reionisation of the universe, the ionising budget of the EoR is still poorly constrained.

* The first question is to assess if the galaxies produce enough hydrogen-ionising photons to reionise the universe and then to sustain this ionised state? Since the radiation is mostly produced by hot, massive, short-lived stars, this raise the question of the star formation in the first galaxies, and for instance the impact of the stellar radiation on the galactic scale star formation.
* A second topic is to understand how much of the radiation could escape into the IGM, and to quantify this. How do the radiation escape? How is it related to the galaxy properties? For example, massive galaxies contain more neutral gas than their smaller counterparts, so it should be easier for the ionising radiation to escape small galaxies, but at the same time, massive galaxies are more luminous, even if they are more rare.

These are the two key questions to understand the ionising budget of the universe during the EoR, and form the core of my research.


Modeling galaxy formation with RAMSES
"""""""""""""""""""""""""""""""""""""

.. figure:: {filename}/img/z9687xHI.png
   :alt: Hydrogen ionised fraction in a typical halo
   :align: right
   :figwidth: 40%
   :width: 95%

   Hydrogen ionised fraction around *z* ~ 6 in a 10\ :sup:`9` M\ :sub:`☉` halo. White is neutral, black is ionised.

I use the :abbr:`AMR (Adaptive Mesh Refinement)` code RAMSES to model and investigate the processes that govern galaxy formation. RAMSES is a grid hydrodynamicals code that follows the evolution of astrophysical fluids in a cosmological context. This allows to compute at the same time the evolution of dark matter (DM), gas and stars. Since recent developments, RAMSES features a module for radiative transfer that can be used to follow altogether the propagation of ionising radiation the detailed ionisation state of the hydrogen and helium around galaxies in simulations.

I perform numerical simulations of individual resolved galaxies using the "zoom" technique. The idea is to simulate a (fairly) large cosmological box with a coarse resolution to select an interesting halo, and then rerun the simulation, but focusing more computational power around that halo to reach very high resolution. For this project, I am focusing on small haloes (10\ :sup:`8` or 10\ :sup:`9` M\ :sub:`☉`), with very high resolution (typically around 10 pc). As I am interested in galaxy formation during the EoR, I run the simulation for one billion year, down to *z* ~ 6.

Even with this high resolution, we cannot completely resolve the formation (or even worse, the internal dynamics) of stars, so we have to use *subgrid models* to model the small scale processes, like star formation, metal ejection by supernovae or energetic events like type II supernovae. It is crucial to take these mechanism into account if we want to model correctly the interstellar medium of high redshift galaxies.

With these tools, I am running the |GARULFO| suite of simulations for my project. This is a series of a limited number of galaxies, simulated with a very high resolution and coupled radiative transfer of ionising radiation.


Escape of ionising radiation and bursty star formation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

One of the goals of the |GARULFO| suite of simulation is to study the amout of ionising photons escaping their home galaxy. The current understanding of reionisation is that at least at early times, small galaxies in low mass haloes were the major contributors to the global ionising budget. It is thus crucial to assess how much radiation can escape those small galaxies.

We have a fine enough time resolution to follow the very high variability of the star formation rate (SFR). One of the results of my project is that for such small galaxies, the SFR varies on timescales of typically 50 - 100 Myr. This is mainly because the star formation (SF) is regulated by the supernovae feedback: after a few tens of Myr, the most massive stars will end their lives and explode in supernovae. This will release a lot of energy and heat the surrounding gas, thus preventing further SF until the gas can cool again and fall on the galaxy.

In the |GARULFO| simulations, we also found that the ionising *escape fraction* (the fraction of emitted photons that escape the halo) varies a lot with time, from nothing to almost 100%, with the timescale, but slightly delayed with respect to the SF. This is most likely due to the fact that ionising radiation is trapped inside the star forming clouds prior to the first supernovae explosions. As soon as the first supernovae goes off, it clears the way for ionising photons to escape. After the SF shuts down, there is no massive star left to produce a significat amount of ionising radiation, and the escape fraction goes down again as the gas cools in the halo.

Some animations illustrating this cycle can be found on `this page <bursty.html>`_.


Previous project: Lyman alpha blobs
-----------------------------------

|lya| blobs are very large, luminous, |lya| emitting nebulae, usually found at high redshift. While these objects denote the presence of large quantities of neutral hydrogen around galaxies (|lya| photons are emitted by the de-excitation of an hydrogen atom), the mechanism powering the |lya| emission is still unclear.

Various scenarios have been suggested to explain the origin of this emission. Among them, I studied the idea that |lya| blobs are tracers of the cosmic web. In this picture, the |lya| radiation is produced by the infall of cosmological filaments on (group of) proto-galaxies. As the gas falls in the dark matter halo, it will radiate its gravitational energy as |lya| photons.

.. figure:: {filename}/img/blob.svg
   :alt: Polarization signal around a simulated |lya| blob.
   :align: right
   :figwidth: 40%
   :width: 95%

   Polarization signal around the modeled |lya| blob.

This scenario has been studied in details in a paper by `Rosdahl & Blaizot (2012) <http://cdsads.u-strasbg.fr/abs/2012MNRAS.423..344R>`_. For my project, I use a Monte-Carlo radiative transfer code called MCLya to investigate the |lya| properties of one of the blob they simulated. I shown that the radiative transfer of |lya| radiation has only a small impact on the size and the shape of the blob.

One of the goal of this project was to get a theoretical understanding of the polarization properties of |lya| radiation emitted by the infalling gas. This was triggered by the observation that |lya| emission in a very massive blob was polarized (`Hayes et al., 2011 <http://cdsads.u-strasbg.fr/abs/2011Natur.476..304H>`_), which has often been interpred as a proof that the |lya| photons are produced in the center of the blob.

In my work, I have shown that a similar polarization can be predicted even if most of the |lya| radiation is produced by infall of the intergalactic gas. These results have been presented at the French Astronomy Meeting in 2014, and a paper has recently been submitted to *Astronomy & Astrophysics*.





.. |lya| replace:: Lyman-α

.. |GARULFO| replace:: :abbr:`GARULFO (Galaxies Reionising the Universe: Light from the First Objects)`
