import kfp
from kfp import components
from kfp import dsl
from kfp.components import create_component_from_func
from kfp.components import InputTextFile, OutputTextFile, OutputBinaryFile, InputBinaryFile


def writedf(output_dataframe_path: OutputBinaryFile()):
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
    df.to_pickle(output_dataframe_path)


def readdf(dataframe_path: InputBinaryFile()): # The "text" input is untyped so that any data can be printed
    import pandas as pd
    # df = pd.DataFrame()
    df = pd.read_pickle(dataframe_path)
    print(df)

write_df_op = create_component_from_func(writedf, base_image='matejcvut/kubeflow-pod:0')
read_df_op = create_component_from_func(readdf, base_image='matejcvut/kubeflow-pod:0')

@dsl.pipeline(
    name="df pipeline",
    description="create dataframe, consume dataframe"
)
def df_pipeline():
    write_df_task = write_df_op()
    read_df_task = read_df_op(write_df_task.output)


if __name__ == "__main__":
    PIPE_DIR = 'pipes-compiled/'
    pipeline_path = PIPE_DIR + df_pipeline.__name__ + '.yaml'
    kfp.compiler.Compiler().compile(df_pipeline, pipeline_path)
