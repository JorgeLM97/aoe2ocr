# AOE2 OCR - Roadmap

## Stage 1 - Ver. 0.1

### Image Parsing Module
- [ ] Take a screenshot of the game and parse the relevant info periodically (1080p) **WIP**

### Build Order Module
- [ ] Hardcode a scouts BO

### In-Game Overlay
- [ ] Make a simple, non-intrusive panel that shows the suggested BO step

### Game Logic Module
- [ ] Evaluate current state from parsed info and provide suggestions on where to send vils

### Quality Assurance
- [ ] Setup a Testing Environment, and create CI tasks. **WIP**

## TBD

### Image Parsing Module
- [ ] Gather info from different resolutions and apply it to the filter
- [ ] HUD Scaling configuration

### Notification Parsing Module
- [ ] Gather from the notifications such as "Castle Built" shown on the screen, to improve the BO suggestions

### Build Order Module
- [ ] Plan a config format for build orders
- [ ] Make a parser to get build orders from a text file

### Info Panel GUI
- [ ] Make a GUI to easily add BOs
- [ ] Make it customizable

### CUDA Based Image Recognition
- [ ] TBD

### Other
- [ ] Localization
- [ ] Civilization Based BO Suggestions
- [ ] Idle Warning
- [ ] Resource Tracking
- [ ] Build Order sharing platform? Integration with existing platform?
