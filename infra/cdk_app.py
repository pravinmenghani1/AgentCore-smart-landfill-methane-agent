# cdk_app.py - AWS CDK deployment template
from aws_cdk import (
    App, Stack, Duration,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets,
)

class LandfillMethaneStack(Stack):
    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        # S3 bucket for logs and evidence
        evidence_bucket = s3.Bucket(
            self, "EvidenceBucket",
            versioned=True,
            lifecycle_rules=[
                s3.LifecycleRule(
                    id="ArchiveOldEvidence",
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.GLACIER,
                            transition_after=Duration.days(90)
                        )
                    ]
                )
            ]
        )
        
        # Lambda function for methane monitoring
        methane_function = _lambda.Function(
            self, "MethaneMonitorFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="main.lambda_handler",
            code=_lambda.Code.from_asset("../src"),
            timeout=Duration.minutes(5),
            environment={
                "EVIDENCE_BUCKET": evidence_bucket.bucket_name
            }
        )
        
        evidence_bucket.grant_write(methane_function)
        
        # EventBridge rule for periodic execution
        rule = events.Rule(
            self, "MethaneMonitorRule",
            schedule=events.Schedule.rate(Duration.minutes(1))
        )
        
        rule.add_target(targets.LambdaFunction(methane_function))

app = App()
LandfillMethaneStack(app, "LandfillMethaneStack")
app.synth()
