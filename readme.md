# Bhargav Ganguly — research profile

A static personal website for GitHub Pages. No build step or JavaScript dependencies are required.

## Local preview

From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765 in a browser. Stop the server with Ctrl+C.

## Editing

- `index.html`: profile, experience, publications, and contact links.
- `css/profile.css`: responsive layout and visual styles.
- `img/`: existing portrait and publication images.

The five additional publications use a native HTML disclosure, so all navigation and content work without JavaScript. Legacy theme assets remain available for older pages.

## Research notes

- `notes/index.html`: Research Notes listing.
- `notes/master-fl/index.html`: visual overview of adapting federated learning to concept drift.
- `notes/dist-ucrl/index.html`: visual overview of communication-efficient parallel reinforcement learning.
- The homepage links to notes from its navigation and a featured blurb.
- Supplied research PDFs in `Bhargav_Ganguly_publications/` are local source material and are ignored by Git. Published notes link to public paper pages.

## Experience timeline logos

Logos are stored locally in `img/logos/` and used to identify educational and professional affiliations. Original colors and proportions are preserved.

- IIT Kanpur: [institute logo page](https://iitk.ac.in/iitk-logo), [image](https://iitk.ac.in/data/media/others/1_0.jpg).
- Purdue: [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Purdue_University_system_logo.svg).
- Amazon: [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Amazon_2024.svg).
- JPMorgan Chase: [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:J_P_Morgan_Chase_Logo_2008_1.svg), historical wordmark.
- Fuzzy Logix: [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Fuzzy_Logix_logo.jpg).

The timeline is ordered by role start date, newest first. Internships during the IIT Kanpur and Purdue degrees are explicitly labeled; academic and employment dates may overlap.

## New visual notes

- `notes/quantum-rl/index.html`: Q-UCRL’s access model, learning cycle, and theoretical horizon dependence. The comparison panel is a schematic, not measured performance.
- `notes/ce-fl/index.html`: cooperative edge training and floating aggregation, illustrated with the paper’s architecture and results plots.
- `img/notes/quantum-rl/interaction.png`: Figure 1, supplied quantum paper, page 4.
- `img/notes/ce-fl/`: Figure 2 (page 2), Figure 3(c), and Figures 4(a–b) (page 14), supplied CE-FL paper.
- All five new images are unmodified figure crops rendered directly from the supplied PDFs at 440 dpi. Source and figure references also appear on the notes. The PDFs remain local and ignored by Git.
- The homepage features the two newest notes; the Notes index lists all four. Each original-research spotlight links to its corresponding note.
