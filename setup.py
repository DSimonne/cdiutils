# CDIUTILS: Utilities for BCDI practitioners

# authors:
#              Clement Atlan, c.atlan@outlook.com
import setuptools

setuptools.setup(
      name='cdiutils',
      version='0.1.4',
      author="Clement Atlan",
      description=(
            "A python package to help Coherent Diffraction Imaging (CDI) "
            "practitioners in their analysis"
      ),
      author_email="c.atlan@outlook.com",
      scripts=[
            "scripts/analyze_bcdi_data.py",
            "scripts/prepare_bcdi_notebooks.py",
            "scripts/prepare_parameter_files.py"
      ],
      packages=setuptools.find_packages(),
      package_data={
        'cdiutils': [
            'process/pynx-id01cdi_template_perlmutter.slurm',
            'process/pynx-id01cdi_template_slurm-nice-devel.slurm',
            'examples/bcdi_pipeline.ipynb',
            'examples/step_by_step_bcdi_analysis.ipynb'
        ],
      },
      include_package_data=True,
      url="https://github.com/clatlan/cdiutils",
      python_requires=">=3.10",
      install_requires=[
            "colorcet>=3.0.0",
            "h5py>=3.6.0",
            "hdf5plugin>=3.2.0",
            "ipykernel",
            "matplotlib>=3.5.2",
            "numpy>=1.23.5",
            "pandas>=1.4.2",
            "paramiko>=2.12.0",
            "ruamel.yaml>=0.17.21",
            "ruamel.yaml.clib>=0.2.7",
            "scikit-image>=0.19.2",
            "scikit-learn>=1.1.3",
            "scipy>=1.8.0",
            "seaborn>=0.12.1",
            "silx>=1.0.0",
            "tabulate",
            "vtk>=9.0.1",
            "xrayutilities>=1.7.3",
            "ipyvolume",
            "ipython_genutils",
            "bokeh",
            "panel",
            "tornado",
      ]
)
