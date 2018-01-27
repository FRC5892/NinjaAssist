package frc.team0000.robot;

import edu.wpi.first.wpilibj.*;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;

public class Robot extends TimedRobot {

    private Joystick stick;

    private  SpeedControllerGroup leftDrive;
    private SpeedControllerGroup rightDrive;
    private DifferentialDrive driveTrain;

    private Timer autonTimer = new Timer();

    @Override
    public void robotInit() {
        stick = new Joystick(0);

        leftDrive = new SpeedControllerGroup(null);
        rightDrive = new SpeedControllerGroup(null);
        driveTrain = new DifferentialDrive(leftDrive, rightDrive);
    }

    @Override
    public void autonomousInit() {
        leftDrive.set(0.5);
        rightDrive.set(0.5);

        autonTimer.reset();
        autonTimer.start();
    }
    
    @Override
    public void autonomousPeriodic() {
        if (autonTimer.hasPeriodPassed(5)) {
            leftDrive.set(0);
            rightDrive.set(0);
        }
    }

    @Override
    public void teleopPeriodic() {
        driveTrain.arcadeDrive(stick.getRawAxis(1), stick.getRawAxis(4));
    }
}