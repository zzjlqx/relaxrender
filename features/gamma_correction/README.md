# 重要！

请务必在项目根目录运行下面几行代码 不然无法测试 ！！！！

**conda env create --file environment.yml**

**activate relaxrender**

**conda install --file requirements.txt -y**

**pip install -e .**



---

render.py 需要写不同的函数（也可以说是接口） 暴露提供给外部（test.py文件）调用

 就像 relaxrender目录下PIONTS.py ...等的文件



test.py 如有不懂可参考tests目录下老师写的

---

测试时在gamma_correction目录下使用 pytest test 命令 目前还不知道参数的作用 你们可以先查

整个项目的测试可以在整个项目根目录使用

pytest --cov-report=html --cov=relaxrender --ignore=tests/test_relaxrender.py tests