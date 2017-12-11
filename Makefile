# Include variables
include config.mk

## env		: Create a conda environment with required installations
.PHONY : env
env : $(ENV_YML)
	conda env create -f $(ENV_YML)

## all		: Run the Jupyter notebooks (in-place)
.PHONY : all
all : 
	jupyter nbconvert --to notebook \
	--execute investors.ipynb \
	--output investors.ipynb \
	--ExecutePreprocessor.timeout=-1
	jupyter nbconvert --to notebook \
	--execute location_time.ipynb \
	--output location_time.ipynb \
	--ExecutePreprocessor.timeout=-1
	jupyter nbconvert --to notebook \
	--execute classification_data_prep.ipynb \
	--output classification_data_prep.ipynb \
	--ExecutePreprocessor.timeout=-1
	jupyter nbconvert --to notebook \
	--execute classification.ipynb \
	--output classification.ipynb \
	--ExecutePreprocessor.timeout=-1
	jupyter nbconvert --to notebook \
	--execute main.ipynb \
	--output main.ipynb \
	--ExecutePreprocessor.timeout=-1

## clean       : Remove auto-generated files.
.PHONY: clean
clean:
	rm -f $(GRAPHICS) $(RESULTS)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<