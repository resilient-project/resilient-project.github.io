---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Resilient (Resilient Energy System Infrastructure Layouts for Industry, E-Fuels and Network Transitions)

## About

The energy transition faces many uncertainties, yet planning tools are often deterministic. Our proposal aims to develop the first truly multi-vector energy infrastructure planning tool that represents this uncertain environment at regional, national, and European levels.

We will build on the widely used, open-source sector-coupled energy planning tool [PyPSA-Eur](https://github.com/pypsa/pypsa-eur), by adding stochastic optimization capabilities and a deeper representation of industry transformation, e-fuel conversion, biomass, and carbon capture infrastructure.

Our analysis will consider uncertainties such as fuel and technology costs, hydrogen availability, network expansion delays for electricity, hydrogen, and carbon dioxide, value chain restructuring in industry, imports of e-fuels and secondary materials, renewables build-out, and social acceptance. Additionally, we will explore novel computational techniques to efficiently address stochastic problems.

For this project, we have assembled a team of leading academic researchers and industry need-owners at the forefront of energy system modeling. We will demonstrate our tool's capabilities through case studies on resilient infrastructure planning in France, Germany, Sweden, and Finland.

To maximize impact, we will organize workshops and training events involving a broader circle of need-owners and stakeholders, ensuring the wide adoption of project results.

<img src="assets/img/pypsaeur.png" alt="pypsa-eur" width="500"/>

<img src="assets/img/resilient-v3.1.png" alt="project-structure" width="480"/>

## Deliverables

D1.1: [Project website](https://resilient-project.github.io/)\
D1.2: [Project data management plan](https://resilient-project.github.io/static/uploads/D1.2_DMP_RESILIENT.pdf)\
D2.1: [Intermediate release of SMS++ and PyPSA integration](https://resilient-project.github.io/static/uploads/D21.pdf)\
D2.3: [Intermediate releases of PyPSA-Eur](https://pypsa-eur.readthedocs.io/en/latest/release_notes.html)\
D3.2: [Interim release of PyPSA-Eur with improved biomass and carbon management representation](https://github.com/PyPSA/pypsa-eur/tree/v0.12.0)\
D*: [Introducing OpenStreetMap high-voltage grid to PyPSA-Eur](https://github.com/PyPSA/pypsa-eur/pull/1079)

## Completed workshops and training events

Workshop with North Rhine-Westphalia industry stakeholders\
*Organised by IN4climate.NRW, 08 October 2024*
- [Project introduction and research goals](https://resilient-project.github.io/static/uploads/resilient-nrw-tom-einführung.pdf)
- [PyPSA-Eur model: overview and applications](https://resilient-project.github.io/static/uploads/Modellanwendung-PyPSA-Eur-TUB.pdf)
- [How does uncertainty impede industrial transformation? (in German)](https://resilient-project.github.io/static/uploads/stakeholderworkshop_FraunhoferISI.pdf)


Energy modelling training workshop with PyPSA & PyPSA-Eur\
*Organised by TransnetBW and TUB, 27-28 January 2025*
- [Invitation](https://www.linkedin.com/feed/update/urn:li:activity:7274361929098317824/)
- [Teaching materials for PyPSA-Eur training](https://docs.google.com/presentation/d/1jqMp5ZYhTRi6gNDoa1UgDzGFLU5ifxeLgfW0R8FBTB4)
- [Teaching materials for PyPSA training](https://irieo.github.io/workshop-pypsa-transnetbw/intro.html)

## Research papers

Millinger et al. [Diversity of biomass usage pathways to achieve emissions targets in the European energy system](https://www.nature.com/articles/s41560-024-01693-6), Nature Energy, 2025

Millinger et al. [Biomass exclusion must be weighed against benefits of carbon supply in European energy system](https://www.nature.com/articles/s41560-024-01685-6), Policy brief in Nature Energy, 2025

Hazem et al. [PyPSA-Earth sector-coupled: A global open-source multi-energy system model showcased for hydrogen applications in countries of the Global South](https://www.sciencedirect.com/science/article/pii/S0306261925000467), Applied Energy, 2025

Xiong et al. [Modelling the high-voltage grid using open data for Europe and beyond](https://arxiv.org/abs/2408.17178), Nature Scientific Data (accepted), 2025

Brown, Neumann & Riepin [Price formation without fuel costs---the interaction of elastic demand with storage bidding](https://arxiv.org/abs/2407.21409), arXiv preprint (in review), 2024

Zachmann, Meißner & Riepin [Mitigating Ukraine's Looming Electricity Crisis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4930511), SSRN preprint (in review), 2024
 

## Research talks, media and public outreach

CETpartnership TRI1 2022 Project Leaders meeting\
*Online, 20 October 2023*\
[RESILIENT project overview](https://resilient-project.github.io/static/uploads/resilient-overview.pdf)

RESILIENT Kick-off meeting\
*Berlin, 22 February 2024*\
[Methanol for hard-to-electrify sectors](https://resilient-project.github.io/static/uploads/brown-methanol.pdf)

Insight Harvesting Workshop of the CETPartnership projects\
*Online, 16 October 2024*\
[Building Resilient Energy Infrastructure: Hydrogen, Import, and Carbon Management Strategies](https://tubcloud.tu-berlin.de/s/kDKgmiHxGGt4FaD/download/20241016-cetp-insight-harvesting.pdf)

CETPartnership workshop on flexibility in integrated industrial energy systems\
*Online, 6 November 2024*\
[Energy flexibility from industrial process heating - Relevance, system impacts and ways forward](https://resilient-project.github.io/static/uploads/Resilient_2024-11-05_FlexibilityFromIndustryInEnergySystem.pdf)

Energy resilience symposium\
*IER, Stuttgart, 11-12 November 2024*\
[Resilient strategies for the European energy system. A case study on 2030 EU policy targets](https://resilient-project.github.io/static/uploads/pci-pmi-2030-targets-presentation.pdf)


## Partners

<img src="assets/img/resilient-partners.png" alt="project-partners" width="500"/>

- At the [Technical University of Berlin (TUB)](https://tu.berlin), the department of Digital Transformation in Energy Systems
is the lead developer of the open energy system modelling framework PyPSA and the high-resolution
model PyPSA-Eur of the European sector-coupled energy system. The group leverages
cutting-edge research from a variety of disciplines to understand the most cost-effective pathways to
reduce greenhouse gas emissions in the energy system. The department will lead the project overall, as
well as the integration of new modelling features and the training of need-owners.

- The team at [University of Pisa (UNIPI)](https://www.unipi.it/) is the core developer of Structured Modelling System
(SMS++), an open-source modelling framework that supports advanced decomposition techniques to
break down computational requirements for large-scale stochastic optimization problems. It will be a key
partner to integrate SMS++ as an backend of PyPSA, needed to enhance its computational capabilities.

- [Fraunhofer ISI](https://www.isi.fraunhofer.de/) offers extensive experience in energy system modelling, in particular with respect to
long-term energy demand from sectors including industry, and the impact of variable renewable energies
in the power system. At Fraunhofer ISI one of the leading industry transformation models,
FORECAST, which has been used in several German and European projects, will be integrated into
PyPSA-Eur to model fuel and process switching in each industrial sector.

- [Chalmers University of Technology](https://www.chalmers.se/) provides extensive expertise in the modelling of energy systems,
model-based analyses of cost-effective usage of biomass in the energy system for achieving climate
targets, as well as modelling of renewable fuels and carbon dioxide capture, usage, transport and
sequestration (CCUTS), and are long-standing contributors to PyPSA-Eur. Chalmers will leverage their
expertise on the most suitable applications of restricted biomass potentials, and the role of CCUTS
infrastructure across different sectors.

- [RISE Research Institutes of Sweden](https://www.ri.se/) works closely with industry and policymakers to accelerate the shift towards sustainable energy systems. Their projects span from developing and demonstrating novel renewable technologies to assessing system-level impacts, bridging the gap between research findings and commercial or public-sector adoption. RISE team brings extensive expertise in energy systems modelling and advanced analyses on cost-effective biomass usage, renewable fuels, and carbon dioxide capture, usage, transport and sequestration.

- [Lappeenranta-Lahti University of Technology (LUT)](https://www.lut.fi/en) is one of the leaders in the research of net-zero
energy systems with an energy system model LUT-ESTM applied to energy transition studies for
dozens of countries across the globe. LUT will bring a global perspective to model the worldwide trading of hydrogen and derivative chemicals and
materials, as well as trade-offs between imports and domestic supply. LUT will also study the role of
sustainable point sources of CO2 on the production of e-fuels and other carbonaceous
materials with emphasis on Finland.

- [TransnetBW](https://www.transnetbw.de/de) is a transmission system operator based in southwest Germany that specialises in the secure
and reliable supply of electricity. With extensive experience in the energy industry, it has conducted
several studies investigating net-zero energy systems using PyPSA-Eur. They will help the consortium
define relevant uncertainties for planners, and play a leading role in the demonstration studies.

- [Électricité de France (EDF)](https://www.edfenergy.com/) is the second world’s leading multinational electricity company, particularly
well established in Europe. Its business covers all electricity-based activities from generation to
distribution, including energy transmission and trading activities. EDF Research and Development
develops models for short to mid-term operation as well as long-term planning of energy systems at
national and European levels and performs techno-economic studies for evaluating impacts of
regulations, analysing transition scenarios, evaluating economic stakes of new models, and analysing
investments in production and storage facilities.

- [IN4climate.NRW](https://www.energy4climate.nrw/industrie-produktion/in4climatenrw) is the initiative for industry transition towards climate neutrality under the umbrella of the state agency NRW.Energy4Climate. IN4climate.NRW works as a think tank and as a working platform
for and with industry, science, and the state government. They will build a bridge to industry needs and federal-state strategies for carbon management and hydrogen.

- [Stockholm Exergi](https://www.stockholmexergi.se/) is an energy company providing district heat and power and waste incineration in
Stockholm, with a pioneering carbon capture research facility that is planned for full-scale operation in
2026 to capture 800 kilotons of biogenic carbon dioxide. They provide expertise and data
validation for modelling bioenergy with carbon capture.

- [ABB Finland](https://new.abb.com/fi) is one of the leaders in electrification and automation, providing technology and
knowledge to dozens of projects contributing to the energy transition of Europe. ABB joins the consortium as an associated partner and
supports data collection, scenario definition and result analysis in terms related to e-fuels production.

## Impressum

Dr. Fabian Neumann\
Dr. Iegor Riepin\
Bobby Xiong\
Prof. Dr. Tom Brown\
[Technische Universität Berlin](https://tu.berlin)
[Fachgebiet Digitaler Wandel in Energiesystemen](https://tu.berlin/ensys/en)\
Institut für Energietechnik\
Fakultät III\
Einsteinufer 25 (TA 8)\
10587 Berlin