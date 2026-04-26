# ISM LLM Wiki

Quartz-powered PhD wiki for **Metal Alloy Processing for In-Space Manufacturing: Investigating Solidification Behaviour Under Microgravity**.

## Local Preview

```bash
npm install
npm run serve
```

The Quartz content folder is generated from the Obsidian vault folders by:

```bash
npm run sync:content
```

Do not edit `content/` directly. Edit the vault notes, then rerun the sync/build command.

## Build

```bash
npm run build
```

The GitHub Pages workflow builds Quartz and deploys the generated `public/` folder.
