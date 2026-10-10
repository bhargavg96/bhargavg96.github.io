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

The six additional publications use a native HTML disclosure, so all navigation and content work without JavaScript. Legacy theme assets remain available for older pages.

## Research notes

- `notes/index.html`: Research Notes listing.
- `notes/master-fl/index.html`: visual overview of adapting federated learning to concept drift.
- `notes/dist-ucrl/index.html`: visual overview of communication-efficient parallel reinforcement learning.
- The homepage links to notes from its navigation and a featured blurb.
- Supplied research PDFs in `Bhargav_Ganguly_publications/` are local source material and are ignored by Git. Published notes link to public paper pages.
