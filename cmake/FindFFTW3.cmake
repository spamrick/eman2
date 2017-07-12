CHECK_REQUIRED_LIB(FFTW3F fftw3f fftw3.h libfftw3f-3 "")
CHECK_REQUIRED_LIB(FFTW3D fftw3 fftw3.h libfftw3-3  "")
ADD_DEFINITIONS(-DUSE_FFTW3)
SET(FFTW_LIBRARIES ${FFTW3F_LIBRARY} ${FFTW3D_LIBRARY})
SET(FFTW_INCLUDE_PATH ${FFTW3_INCLUDE_PATH})

if(ENABLE_CONDA)
	message("FFTW_LIBRARIES: ${FFTW_LIBRARIES}")
	message("FFTW_INCLUDE_PATH: ${FFTW_INCLUDE_PATH}")
endif()
