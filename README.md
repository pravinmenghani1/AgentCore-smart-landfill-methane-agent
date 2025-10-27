# Smart Landfill Methane Capture & Alarm Agent

A predictive AI agent system powered by **AgentCore** and **Strands SDK** for monitoring methane emissions at landfills and automatically triggering vent/flare actions when dangerous levels are detected.

## Features

- **AgentCore Orchestration**: Multi-agent system with message-based communication
- **Strands SDK Integration**: Advanced reasoning, validation, and action engines
- Real-time methane sensor simulation with predictive analytics
- AI-powered risk assessment with confidence scoring
- Automated safety validation and regulatory compliance
- Distributed action execution with audit trails
- Enhanced compliance evidence generation

## Architecture

```
[SENSOR SIMULATOR] ---> [PLANNER AGENT] ---> [SAFETY GUARD] ---> [EXECUTOR] ---> [EVIDENCE]
        |                    |                    |                  |              |
        |              Strands Reasoning    Strands Validation  Strands Action  Strands Docs
        |                    |                    |                  |              |
        +-------------------> AgentCore Orchestrator <---------------------------------+
```

## Technology Stack

- **AgentCore**: Agent lifecycle management and message orchestration
- **Strands SDK**: AI reasoning, validation, action, and document engines
- **Python**: Core implementation language
- **ReportLab**: PDF generation for compliance reports

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the AgentCore system:**
   ```bash
   python src/main.py
   ```

3. **View logs:**
   - Action logs: `logs/actions/`
   - Evidence reports: `logs/evidence/`

## Configuration

### AgentCore Configuration
- Agent registration and message routing
- Distributed execution management
- Inter-agent communication protocols

### Strands SDK Configuration
Edit `src/strands_config.py` to adjust:
- Reasoning engine models and thresholds
- Validation rules and regulatory frameworks
- Action execution parameters
- Document generation templates

### System Configuration
Edit `src/config.py` for:
- Methane threshold levels (default: 1500 ppm)
- Prediction horizon (default: 3 hours)
- Simulation speed and log directories

## Agent Components

### **Planner Agent** (Strands Reasoning Engine)
- Processes methane readings using AI models
- Generates predictions with confidence scores
- Creates action plans with detailed reasoning

### **Safety Guard** (Strands Validation Engine)
- Validates plans against regulatory constraints
- Ensures compliance with EPA standards
- Provides detailed validation reports

### **Executor Agent** (Strands Action Engine)
- Executes validated actions through simulation
- Logs all operations with metadata
- Manages action cooldowns and timeouts

### **Evidence Agent** (Strands Document Engine)
- Generates compliance documentation automatically
- Creates audit-ready PDF and JSON reports
- Maintains regulatory retention policies

## Message Flow

1. **Sensor Reading**: Continuous methane monitoring
2. **AI Analysis**: Strands reasoning engine predicts risk
3. **Safety Validation**: Regulatory compliance checking
4. **Action Execution**: Automated response with logging
5. **Evidence Generation**: Compliance documentation

## Testing

```bash
python -m pytest tests/
```

## Deployment

The system includes AWS CDK templates for cloud deployment with:
- Lambda functions for agent execution
- S3 storage for evidence and logs
- EventBridge for scheduling and orchestration

## License

MIT License
