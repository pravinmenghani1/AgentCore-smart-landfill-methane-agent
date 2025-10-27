# Smart Landfill Methane Capture & Alarm Agent

A predictive AI agent system for monitoring methane emissions at landfills and automatically triggering vent/flare actions when dangerous levels are detected.

## Features

- Real-time methane sensor simulation
- Predictive risk assessment using ML algorithms
- Safety validation and constraint checking
- Automated action execution and logging
- Compliance evidence generation (PDF + JSON)
- Audit-ready documentation

## Architecture

```
[SENSOR SIMULATOR] ---> [PLANNER AGENT] ---> [SAFETY GUARD] ---> [EXECUTOR] ---> [EVIDENCE]
        |                                                         |
        +--------------------> LOGS / S3 -------------------------+
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the simulation:**
   ```bash
   python src/main.py
   ```

3. **View logs:**
   - Action logs: `logs/actions/`
   - Evidence reports: `logs/evidence/`

## Configuration

Edit `src/config.py` to adjust:
- Methane threshold levels (default: 1500 ppm)
- Prediction horizon (default: 3 hours)
- Simulation speed
- Log directories

## Components

- **Sensor Simulator**: Generates realistic methane readings with configurable spikes
- **Planner Agent**: Predicts methane risk and determines required actions
- **Safety Guard**: Validates actions against regulatory constraints
- **Executor Agent**: Logs simulated actuation decisions
- **Evidence Agent**: Generates compliance documentation

## Testing

```bash
python -m pytest tests/
```

## License

MIT License
