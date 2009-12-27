import direct.directbase.DirectStart


environment = loader.loadModel('models/environment')
environment.reparentTo(render)


def rotate(task):
    base.camera.setHpr(task.time * 10, 0, 0)
    return task.cont

taskMgr.add(rotate, 'rotate')

run()
