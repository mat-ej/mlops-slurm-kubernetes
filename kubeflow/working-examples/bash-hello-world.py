import kfp
from kfp import dsl
def echo_op():
    return dsl.ContainerOp(
        name='echo',
        image='library/bash:4.4.23',
        command=['sh', '-c'],
        arguments=['echo "hello world"']
    )


@dsl.pipeline(
    name='my-first-pipeline',
    description='A hello world pipeline.'
)
def hello_world_pipeline():
    echo_task = echo_op()


if __name__ == '__main__':
    PIPE_DIR = 'pipes-compiled/'
    pipeline_path = PIPE_DIR + hello_world_pipeline.__name__ + '.yaml'
    kfp.compiler.Compiler().compile(hello_world_pipeline, pipeline_path)
