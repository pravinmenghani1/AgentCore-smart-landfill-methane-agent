# Architecture Overview

## System Flow

```
[SENSOR SIMULATOR] ---> [PLANNER AGENT] ---> [SAFETY GUARD] ---> [EXECUTOR] ---> [EVIDENCE]
        |                                                         |
        +--------------------> LOGS / S3 -------------------------+
```

## Components

### Sensor Simulator
- Generates realistic methane readings with configurable parameters
- Simulates normal operations and dangerous spikes
- Provides continuous data stream for the system

### Planner Agent
- Analyzes current and historical methane readings
- Predicts future methane levels using simple ML algorithms
- Determines when vent/flare actions are needed
- Generates action plans with timestamps and risk assessments

### Safety Guard
- Validates all proposed actions against safety constraints
- Ensures regulatory compliance
- Prevents unsafe or impossible operations
- Logs validation failures for audit purposes

### Executor Agent
- Receives validated action plans
- Simulates equipment actuation (vent/flare operations)
- Logs all actions with detailed metadata
- Provides real-time status updates

### Evidence Agent
- Generates compliance documentation for all actions
- Creates PDF reports for regulatory submissions
- Maintains JSON logs for system integration
- Ensures audit trail completeness

## Data Flow

1. **Sensor Reading**: Methane levels are continuously monitored
2. **Risk Assessment**: Planner evaluates current and predicted risk
3. **Safety Validation**: Guard ensures proposed actions are safe
4. **Action Execution**: Executor logs simulated equipment operations
5. **Evidence Generation**: Compliance documentation is automatically created

## Configuration

The system is highly configurable through `config.py`:
- Methane threshold levels
- Prediction algorithms
- Logging destinations
- Simulation parameters
