from i2clibraries import i2c_hmc5883l

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)

hmc5883l.setContinuousMode()

(x, y, z) = hmc5883l.getAxes()
