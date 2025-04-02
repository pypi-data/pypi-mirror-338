choldate
========

Somewhat fast updating and downdating of Cholesky factors in Python

##installation

Clone the GitHub repository and install from source, e.g.,

1. `git clone git://github.com/jcrudy/choldate.git`
2. `cd choldate && make sync && make install-pre-commit && make`

The `Makefile` makes it easy to perform the most common operations:
* `make check-all` runs linting and `uv.lock` checks
* `make check-lint` checks for linting issues
* `make check-lock` verifies the `uv.lock` is aligned to `pyproject.toml`
* `make clean` cleans the virtual environment and caches
* `make default` runs a default set of checks on the code
* `make fix-all` formats the code, fixes lint errors and runs locks `uv.lock` to `pyproject.toml`
* `make fix-format` formats the code
* `make fix-lint` fixes linting issues
* `make fix-lint-unsafe` fixes linting issues potentially adding inadvertant bugs
* `make help` outputs the different make options
* `make install` build install the distribution
* `make install-pre-commit` installs pre-commit hooks
* `make lock` locks `uv.lock` to `pyproject.toml`
* `make install-pre-commit` installs pre-commit hooks
* `make run-tests` runs the unit tests
* `make sync` syncs the python environment with `uv.lock`

`.vscode/settings.json` is set so that unit tests can be run without further configuration.

##usage
```python
from choldate import cholupdate, choldowndate
import numpy

#Create a random positive definite matrix, V
numpy.random.seed(1)
X = numpy.random.normal(size=(100,10))
V = numpy.dot(X.transpose(),X)

#Calculate the upper Cholesky factor, R
R = numpy.linalg.cholesky(V).transpose()

#Create a random update vector, u
u = numpy.random.normal(size=R.shape[0])

#Calculate the updated positive definite matrix, V1, and its Cholesky factor, R1
V1 = V + numpy.outer(u,u)
R1 = numpy.linalg.cholesky(V1).transpose()

#The following is equivalent to the above
R1_ = R.copy()
cholupdate(R1_,u.copy())
assert(numpy.all((R1 - R1_)**2 < 1e-16))

#And downdating is the inverse of updating
R_ = R1.copy()
choldowndate(R_,u.copy())
assert(numpy.all((R - R_)**2 < 1e-16))
```


Important Note
==============

This modules was originally developed by modusdatascience and the original repo can be found at
https://github.com/modusdatascience/choldate

This fork is being maintained by jamieleecho.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.