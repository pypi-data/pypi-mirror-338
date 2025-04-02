# Doxygen stubs generation
import numpy
import typing
AvoidSelfCollisionsDynamicsConstraint = typing.NewType("AvoidSelfCollisionsDynamicsConstraint", None)
AvoidSelfCollisionsKinematicsConstraint = typing.NewType("AvoidSelfCollisionsKinematicsConstraint", None)
AxisAlignTask = typing.NewType("AxisAlignTask", None)
AxisesMask = typing.NewType("AxisesMask", None)
CentroidalMomentumTask = typing.NewType("CentroidalMomentumTask", None)
CoMPolygonConstraint = typing.NewType("CoMPolygonConstraint", None)
CoMTask = typing.NewType("CoMTask", None)
Collision = typing.NewType("Collision", None)
ConeConstraint = typing.NewType("ConeConstraint", None)
Contact = typing.NewType("Contact", None)
Contact6D = typing.NewType("Contact6D", None)
CubicSpline = typing.NewType("CubicSpline", None)
CubicSpline3D = typing.NewType("CubicSpline3D", None)
Distance = typing.NewType("Distance", None)
DistanceTask = typing.NewType("DistanceTask", None)
DynamicsCoMTask = typing.NewType("DynamicsCoMTask", None)
DynamicsConstraint = typing.NewType("DynamicsConstraint", None)
DynamicsFrameTask = typing.NewType("DynamicsFrameTask", None)
DynamicsGearTask = typing.NewType("DynamicsGearTask", None)
DynamicsJointsTask = typing.NewType("DynamicsJointsTask", None)
DynamicsOrientationTask = typing.NewType("DynamicsOrientationTask", None)
DynamicsPositionTask = typing.NewType("DynamicsPositionTask", None)
DynamicsRelativeFrameTask = typing.NewType("DynamicsRelativeFrameTask", None)
DynamicsRelativeOrientationTask = typing.NewType("DynamicsRelativeOrientationTask", None)
DynamicsRelativePositionTask = typing.NewType("DynamicsRelativePositionTask", None)
DynamicsSolver = typing.NewType("DynamicsSolver", None)
DynamicsSolverResult = typing.NewType("DynamicsSolverResult", None)
DynamicsTask = typing.NewType("DynamicsTask", None)
DynamicsTorqueTask = typing.NewType("DynamicsTorqueTask", None)
Exception = typing.NewType("Exception", None)
Expression = typing.NewType("Expression", None)
ExternalWrenchContact = typing.NewType("ExternalWrenchContact", None)
Flags = typing.NewType("Flags", None)
Footstep = typing.NewType("Footstep", None)
Footsteps = typing.NewType("Footsteps", None)
FootstepsPlanner = typing.NewType("FootstepsPlanner", None)
FootstepsPlannerNaive = typing.NewType("FootstepsPlannerNaive", None)
FootstepsPlannerRepetitive = typing.NewType("FootstepsPlannerRepetitive", None)
FrameTask = typing.NewType("FrameTask", None)
GearTask = typing.NewType("GearTask", None)
HumanoidParameters = typing.NewType("HumanoidParameters", None)
HumanoidRobot = typing.NewType("HumanoidRobot", None)
HumanoidRobot_Side = typing.NewType("HumanoidRobot_Side", None)
Integrator = typing.NewType("Integrator", None)
IntegratorTrajectory = typing.NewType("IntegratorTrajectory", None)
JointSpaceHalfSpacesConstraint = typing.NewType("JointSpaceHalfSpacesConstraint", None)
JointsTask = typing.NewType("JointsTask", None)
KinematicsConstraint = typing.NewType("KinematicsConstraint", None)
KinematicsSolver = typing.NewType("KinematicsSolver", None)
KineticEnergyRegularizationTask = typing.NewType("KineticEnergyRegularizationTask", None)
LIPM = typing.NewType("LIPM", None)
LIPMTrajectory = typing.NewType("LIPMTrajectory", None)
LineContact = typing.NewType("LineContact", None)
ManipulabilityTask = typing.NewType("ManipulabilityTask", None)
OrientationTask = typing.NewType("OrientationTask", None)
PointContact = typing.NewType("PointContact", None)
PolygonConstraint = typing.NewType("PolygonConstraint", None)
Polynom = typing.NewType("Polynom", None)
PositionTask = typing.NewType("PositionTask", None)
Prioritized = typing.NewType("Prioritized", None)
Problem = typing.NewType("Problem", None)
ProblemConstraint = typing.NewType("ProblemConstraint", None)
ProblemPolynom = typing.NewType("ProblemPolynom", None)
PuppetContact = typing.NewType("PuppetContact", None)
QPError = typing.NewType("QPError", None)
RegularizationTask = typing.NewType("RegularizationTask", None)
RelativeFrameTask = typing.NewType("RelativeFrameTask", None)
RelativeOrientationTask = typing.NewType("RelativeOrientationTask", None)
RelativePositionTask = typing.NewType("RelativePositionTask", None)
RobotWrapper = typing.NewType("RobotWrapper", None)
RobotWrapper_State = typing.NewType("RobotWrapper_State", None)
Segment = typing.NewType("Segment", None)
Sparsity = typing.NewType("Sparsity", None)
SparsityInterval = typing.NewType("SparsityInterval", None)
Support = typing.NewType("Support", None)
Supports = typing.NewType("Supports", None)
SwingFoot = typing.NewType("SwingFoot", None)
SwingFootCubic = typing.NewType("SwingFootCubic", None)
SwingFootCubicTrajectory = typing.NewType("SwingFootCubicTrajectory", None)
SwingFootQuintic = typing.NewType("SwingFootQuintic", None)
SwingFootQuinticTrajectory = typing.NewType("SwingFootQuinticTrajectory", None)
SwingFootTrajectory = typing.NewType("SwingFootTrajectory", None)
Task = typing.NewType("Task", None)
TaskContact = typing.NewType("TaskContact", None)
Variable = typing.NewType("Variable", None)
WPGTrajectory = typing.NewType("WPGTrajectory", None)
WPGTrajectoryPart = typing.NewType("WPGTrajectoryPart", None)
WalkPatternGenerator = typing.NewType("WalkPatternGenerator", None)
WalkTasks = typing.NewType("WalkTasks", None)
WheelTask = typing.NewType("WheelTask", None)
boost_type_index = typing.NewType("boost_type_index", None)
map_indexing_suite_map_string_double_entry = typing.NewType("map_indexing_suite_map_string_double_entry", None)
map_string_double = typing.NewType("map_string_double", None)
std_type_index = typing.NewType("std_type_index", None)
vector_Collision = typing.NewType("vector_Collision", None)
vector_Distance = typing.NewType("vector_Distance", None)
vector_MatrixXd = typing.NewType("vector_MatrixXd", None)
class AvoidSelfCollisionsDynamicsConstraint:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  self_collisions_margin: float # double
  """
  Margin for self collisions [m].
  """

  self_collisions_trigger: float # double
  """
  Distance that triggers the constraint [m].
  """


class AvoidSelfCollisionsKinematicsConstraint:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  self_collisions_margin: float # double
  """
  Margin for self collisions [m].
  """

  self_collisions_trigger: float # double
  """
  Distance that triggers the constraint [m].
  """


class AxisAlignTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def AxisAlignTask(
    self,
    frame_index: any, # pinocchio::FrameIndex
    axis_frame: numpy.ndarray, # Eigen::Vector3d
    targetAxis_world: numpy.ndarray, # Eigen::Vector3d
  ) -> any:
    ...

  axis_frame: numpy.ndarray # Eigen::Vector3d
  """
  Axis in the frame.
  """

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_index: any # pinocchio::FrameIndex
  """
  Target frame.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  targetAxis_world: numpy.ndarray # Eigen::Vector3d
  """
  Target axis in the world.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class AxisesMask:
  R_custom_world: numpy.ndarray # Eigen::Matrix3d
  """
  Rotation from world to custom rotation (provided by the user)
  """

  R_local_world: numpy.ndarray # Eigen::Matrix3d
  """
  Rotation from world to local frame (provided by task)
  """

  def AxisesMask(
    self,
  ) -> any:
    ...

  def apply(
    self,
    M: numpy.ndarray, # Eigen::MatrixXd
  ) -> numpy.ndarray:
    """
    Apply the masking to a given matrix.
    
    :param numpy.ndarray M: the matrix to be masked (3xn)
    """
    ...

  def set_axises(
    self,
    axises: str, # std::string
    frame_: any, # placo::tools::AxisesMask::ReferenceFrame
  ) -> None:
    """
    Sets the axises to be masked (kept), for example "xy".
    
    :param str axises: axises to be kept 
    
    :param any frame_: the reference frame where the masking is done (task, local or custom)
    """
    ...


class CentroidalMomentumTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  L_world: numpy.ndarray # Eigen::Vector3d
  """
  Target centroidal angular momentum in the world.
  """

  def CentroidalMomentumTask(
    self,
    L_world: numpy.ndarray, # Eigen::Vector3d
  ) -> any:
    """
    See KinematicsSolver::add_centroidal_momentum_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Axises mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class CoMPolygonConstraint:
  def CoMPolygonConstraint(
    self,
    polygon: list[numpy.ndarray], # const std::vector< Eigen::Vector2d > &
    margin: float = 0., # double
  ) -> any:
    """
    Ensures that the CoM (2D) lies inside the given polygon.
    
    :param list[numpy.ndarray] polygon: Clockwise polygon
    """
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  dcm: bool # bool
  """
  If set to true, the DCM will be used instead of the CoM.
  """

  margin: float # double
  """
  Margin for the polygon constraint (minimum distance between the CoM and the polygon)
  """

  name: str # std::string
  """
  Object name.
  """

  omega: float # double
  """
  If DCM mode is enabled, the constraint will be applied on the DCM instead of the CoM with the following omega (sqrt(g / h))
  """

  polygon: list[numpy.ndarray] # std::vector< Eigen::Vector2d >
  """
  Clockwise polygon.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class CoMTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def CoMTask(
    self,
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> any:
    """
    See KinematicsSolver::add_com_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target_world: numpy.ndarray # Eigen::Vector3d
  """
  Target for the CoM in the world.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class Collision:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  bodyA: str # std::string
  """
  Name of the body A.
  """

  bodyB: str # std::string
  """
  Name of the body B.
  """

  def get_contact(
    arg1: Collision,
    arg2: int,
  ) -> numpy.ndarray:
    ...

  objA: int # int
  """
  Index of object A in the collision geometry.
  """

  objB: int # int
  """
  Index of object B in the collision geometry.
  """

  parentA: any # pinocchio::JointIndex
  """
  The joint parent of body A.
  """

  parentB: any # pinocchio::JointIndex
  """
  The joint parent of body B.
  """


class ConeConstraint:
  N: int # int
  """
  Number of slices used to discretize the cone.
  """

  def ConeConstraint(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
    angle_max: float, # double
  ) -> any:
    """
    With a cone constraint, the z-axis of frame a and frame b should remaine within a cone of angle angle_max.
    
    :param any frame_a: 
    
    :param any frame_b: 
    
    :param float angle_max:
    """
    ...

  angle_max: float # double
  """
  Maximum angle allowable by the cone constraint (between z-axis of frame_a and frame_b)
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  range: float # double
  """
  Range of the cone discretization (in radians). The cone is discretized in [-range, range] around the current orientation.
  """


class Contact:
  def Contact(
    self,
  ) -> any:
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """


class Contact6D:
  def Contact6D(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
    unilateral: bool, # bool
  ) -> any:
    """
    see DynamicsSolver::add_fixed_planar_contact and DynamicsSolver::add_unilateral_planar_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  length: float # double
  """
  Rectangular contact length along local x-axis.
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  def orientation_task(
    arg1: Contact6D,
  ) -> DynamicsOrientationTask:
    ...

  def position_task(
    arg1: Contact6D,
  ) -> DynamicsPositionTask:
    ...

  unilateral: bool # bool
  """
  true for unilateral contact with the ground
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  width: float # double
  """
  Rectangular contact width along local y-axis.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """

  def zmp(
    self,
  ) -> numpy.ndarray:
    """
    Returns the contact ZMP in the local frame.
    """
    ...


class CubicSpline:
  def CubicSpline(
    self,
    angular: bool = False, # bool
  ) -> any:
    ...

  def acc(
    self,
    x: float, # double
  ) -> float:
    """
    Retrieve acceleration at a given time.
    """
    ...

  def add_point(
    self,
    t: float, # double
    x: float, # double
    dx: float, # double
  ) -> None:
    """
    Adds a point in the spline.
    
    :param float t: time 
    
    :param float x: value 
    
    :param float dx: speed
    """
    ...

  def clear(
    self,
  ) -> None:
    """
    Clears the spline.
    """
    ...

  def duration(
    self,
  ) -> float:
    """
    Spline duration.
    """
    ...

  def pos(
    self,
    t: float, # double
  ) -> float:
    """
    Retrieve the position at a given time.
    
    :param float t: time
    """
    ...

  def vel(
    self,
    x: float, # double
  ) -> float:
    """
    Retrieve velocity at a given time.
    """
    ...


class CubicSpline3D:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def acc(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    """
    Returns the spline accleeration at time t.
    
    :param float t: time
    """
    ...

  def add_point(
    self,
    t: float, # double
    x: numpy.ndarray, # Eigen::Vector3d
    dx: numpy.ndarray, # Eigen::Vector3d
  ) -> None:
    """
    Adds a point.
    
    :param float t: time 
    
    :param numpy.ndarray x: value (3D vector) 
    
    :param numpy.ndarray dx: velocity (3D vector)
    """
    ...

  def clear(
    self,
  ) -> None:
    """
    Clears the spline.
    """
    ...

  def duration(
    self,
  ) -> float:
    """
    Spline duration.
    """
    ...

  def pos(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    """
    Returns the spline value at time t.
    
    :param float t: time
    """
    ...

  def vel(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    """
    Returns the spline velocity at time t.
    
    :param float t: time
    """
    ...


class Distance:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  min_distance: float # double
  """
  Current minimum distance between the two objects.
  """

  objA: int # int
  """
  Index of object A in the collision geometry.
  """

  objB: int # int
  """
  Index of object B in the collision geometry.
  """

  parentA: any # pinocchio::JointIndex
  """
  Parent joint of body A.
  """

  parentB: any # pinocchio::JointIndex
  """
  Parent joint of body B.
  """

  pointA: numpy.ndarray # Eigen::Vector3d
  """
  Point of object A considered.
  """

  pointB: numpy.ndarray # Eigen::Vector3d
  """
  Point of object B considered.
  """


class DistanceTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def DistanceTask(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
    distance: float, # double
  ) -> any:
    """
    see KinematicsSolver::add_distance_task
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  distance: float # double
  """
  Target distance between A and B.
  """

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_a: any # pinocchio::FrameIndex
  """
  Frame A.
  """

  frame_b: any # pinocchio::FrameIndex
  """
  Frame B.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class DynamicsCoMTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
    arg2: numpy.ndarray,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  ddtarget_world: numpy.ndarray # Eigen::Vector3d
  """
  Target acceleration in the world.
  """

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  dtarget_world: numpy.ndarray # Eigen::Vector3d
  """
  Target velocity to reach in robot frame.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Axises mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target_world: numpy.ndarray # Eigen::Vector3d
  """
  Target to reach in world frame.
  """


class DynamicsConstraint:
  def __init__(
  ) -> any:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class DynamicsFrameTask:
  T_world_frame: any

  def __init__(
    arg1: object,
  ) -> None:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    position_weight: float = 1.0, # double
    orientation_weight: float = 1.0, # double
  ) -> None:
    """
    Configures the frame task.
    
    :param str name: task name 
    
    :param str priority: task priority 
    
    :param float position_weight: weight for the position task 
    
    :param float orientation_weight: weight for the orientation task
    """
    ...

  def orientation(
    arg1: DynamicsFrameTask,
  ) -> DynamicsOrientationTask:
    ...

  def position(
    arg1: DynamicsFrameTask,
  ) -> DynamicsPositionTask:
    ...


class DynamicsGearTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
  ) -> None:
    ...

  def add_gear(
    self,
    target: str, # std::string
    source: str, # std::string
    ratio: float, # double
  ) -> None:
    """
    Adds a gear constraint, you can add multiple source for the same target, they will be summed.
    
    :param str target: target joint 
    
    :param str source: source joint 
    
    :param float ratio: ratio
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def set_gear(
    self,
    target: str, # std::string
    source: str, # std::string
    ratio: float, # double
  ) -> None:
    """
    Sets a gear constraint.
    
    :param str target: target joint 
    
    :param str source: source joint 
    
    :param float ratio: ratio
    """
    ...


class DynamicsJointsTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  def get_joint(
    self,
    joint: str, # std::string
  ) -> float:
    """
    Returns the current target position of a joint.
    
    :param str joint: joint name
    """
    ...

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def set_joint(
    self,
    joint: str, # std::string
    target: float, # double
    velocity: float = 0., # double
    acceleration: float = 0., # double
  ) -> None:
    """
    Sets the target for a given joint.
    
    :param str joint: joint name 
    
    :param float target: target position 
    
    :param float velocity: target velocity 
    
    :param float acceleration: target acceleration
    """
    ...

  def set_joints(
    arg1: DynamicsJointsTask,
    arg2: dict,
  ) -> None:
    ...

  def set_joints_velocities(
    arg1: DynamicsJointsTask,
    arg2: dict,
  ) -> None:
    ...


class DynamicsOrientationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  R_world_frame: numpy.ndarray # Eigen::Matrix3d
  """
  Target orientation.
  """

  def __init__(
    arg1: object,
    arg2: int,
    arg3: numpy.ndarray,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  domega_world: numpy.ndarray # Eigen::Vector3d
  """
  Target angular acceleration.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  omega_world: numpy.ndarray # Eigen::Vector3d
  """
  Target angular velocity.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class DynamicsPositionTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
    arg2: int,
    arg3: numpy.ndarray,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  ddtarget_world: numpy.ndarray # Eigen::Vector3d
  """
  Target acceleration in the world.
  """

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  dtarget_world: numpy.ndarray # Eigen::Vector3d
  """
  Target velocity in the world.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  frame_index: any # pinocchio::FrameIndex
  """
  Frame.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target_world: numpy.ndarray # Eigen::Vector3d
  """
  Target position in the world.
  """


class DynamicsRelativeFrameTask:
  T_a_b: any

  def __init__(
    arg1: object,
  ) -> None:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    position_weight: float = 1.0, # double
    orientation_weight: float = 1.0, # double
  ) -> None:
    """
    Configures the relative frame task.
    
    :param str name: task name 
    
    :param str priority: task priority 
    
    :param float position_weight: weight for the position task 
    
    :param float orientation_weight: weight for the orientation task
    """
    ...

  def orientation(
    arg1: DynamicsRelativeFrameTask,
  ) -> DynamicsRelativeOrientationTask:
    ...

  def position(
    arg1: DynamicsRelativeFrameTask,
  ) -> DynamicsRelativePositionTask:
    ...


class DynamicsRelativeOrientationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  R_a_b: numpy.ndarray # Eigen::Matrix3d
  """
  Target relative orientation.
  """

  def __init__(
    arg1: object,
    arg2: int,
    arg3: int,
    arg4: numpy.ndarray,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  domega_a_b: numpy.ndarray # Eigen::Vector3d
  """
  Target relative angular velocity.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  omega_a_b: numpy.ndarray # Eigen::Vector3d
  """
  Target relative angular velocity.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class DynamicsRelativePositionTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
    arg2: int,
    arg3: int,
    arg4: numpy.ndarray,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  ddtarget: numpy.ndarray # Eigen::Vector3d
  """
  Target relative acceleration.
  """

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  dtarget: numpy.ndarray # Eigen::Vector3d
  """
  Target relative velocity.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target: numpy.ndarray # Eigen::Vector3d
  """
  Target relative position.
  """


class DynamicsSolver:
  def DynamicsSolver(
    self,
    robot: RobotWrapper, # placo::model::RobotWrapper
  ) -> any:
    ...

  def add_avoid_self_collisions_constraint(
    self,
  ) -> AvoidSelfCollisionsDynamicsConstraint:
    """
    Adds a constraint to the solver.
    """
    ...

  def add_com_task(
    self,
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> DynamicsCoMTask:
    """
    Adds a center of mass (in the world) task.
    
    :param numpy.ndarray target_world: target (in the world)
    """
    ...

  def add_constraint(
    self,
    constraint: DynamicsConstraint, # placo::dynamics::Constraint
  ) -> None:
    """
    Adds a custom constraint to the solver.
    
    :param DynamicsConstraint constraint: constraint
    """
    ...

  def add_external_wrench_contact(
    self,
    frame_index: any, # pinocchio::FrameIndex
    reference: any = None, # pinocchio::ReferenceFrame (default: pinocchio::LOCAL_WORLD_ALIGNED)
  ) -> ExternalWrenchContact:
    """
    Adds an external wrench.
    
    :param any frame_index: 
    
    :param any reference:
    """
    ...

  def add_fixed_contact(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
  ) -> Contact6D:
    """
    Adds a fixed contact.
    
    :param DynamicsFrameTask frame_task: the associated frame task
    """
    ...

  def add_frame_task(
    self,
    frame_name: str, # std::string
    T_world_frame: numpy.ndarray, # Eigen::Affine3d
  ) -> DynamicsFrameTask:
    """
    Adds a frame task, which is a pseudo-task packaging position and orientation, resulting in a decoupled task.
    
    :param numpy.ndarray T_world_frame: target transformation in the world
    """
    ...

  def add_gear_task(
    self,
  ) -> DynamicsGearTask:
    """
    Adds a gear task, allowing replication of a joint. This can be used to implement timing belt, if coupled with an internal force.
    """
    ...

  def add_joints_task(
    self,
  ) -> DynamicsJointsTask:
    """
    Adds a joints task.
    """
    ...

  def add_line_contact(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
  ) -> LineContact:
    """
    Adds a fixed line contact.
    
    :param DynamicsFrameTask frame_task: associated frame task
    """
    ...

  def add_orientation_task(
    self,
    frame_name: str, # std::string
    R_world_frame: numpy.ndarray, # Eigen::Matrix3d
  ) -> DynamicsOrientationTask:
    """
    Adds an orientation (in the world) task.
    
    :param numpy.ndarray R_world_frame: target world orientation
    """
    ...

  def add_planar_contact(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
  ) -> Contact6D:
    """
    Adds a planar contact, which is unilateral in the sense of the local body z-axis.
    
    :param DynamicsFrameTask frame_task: associated frame task
    """
    ...

  def add_point_contact(
    self,
    position_task: DynamicsPositionTask, # placo::dynamics::PositionTask
  ) -> PointContact:
    """
    Adds a point contact.
    
    :param DynamicsPositionTask position_task: the associated position task
    """
    ...

  def add_position_task(
    self,
    frame_name: str, # std::string
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> DynamicsPositionTask:
    """
    Adds a position (in the world) task.
    
    :param numpy.ndarray target_world: target position in the world
    """
    ...

  def add_puppet_contact(
    self,
  ) -> PuppetContact:
    """
    Adds a puppet contact, this will add some free contact forces for the whole system, allowing it to be controlled freely.
    """
    ...

  def add_relative_frame_task(
    self,
    frame_a_name: str, # std::string
    frame_b_name: str, # std::string
    T_a_b: numpy.ndarray, # Eigen::Affine3d
  ) -> DynamicsRelativeFrameTask:
    """
    Adds a relative frame task, which is a pseudo-task packaging relative position and orientation tasks.
    
    :param numpy.ndarray T_a_b: target transformation value for b frame in a
    """
    ...

  def add_relative_orientation_task(
    self,
    frame_a_name: str, # std::string
    frame_b_name: str, # std::string
    R_a_b: numpy.ndarray, # Eigen::Matrix3d
  ) -> DynamicsRelativeOrientationTask:
    """
    Adds a relative orientation task.
    
    :param numpy.ndarray R_a_b: target value for the orientation of b frame in a
    """
    ...

  def add_relative_position_task(
    self,
    frame_a_name: str, # std::string
    frame_b_name: str, # std::string
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> DynamicsRelativePositionTask:
    """
    Adds a relative position task.
    """
    ...

  def add_task(
    self,
    task: DynamicsTask, # placo::dynamics::Task
  ) -> None:
    """
    Adds a custom task to the solver.
    
    :param DynamicsTask task: task
    """
    ...

  def add_task_contact(
    self,
    task: DynamicsTask, # placo::dynamics::Task
  ) -> TaskContact:
    """
    Adds contact forces associated with any given task.
    
    :param DynamicsTask task: task
    """
    ...

  def add_torque_task(
    self,
  ) -> DynamicsTorqueTask:
    """
    Adds a torque task.
    """
    ...

  def add_unilateral_line_contact(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
  ) -> LineContact:
    """
    Adds a unilateral line contact, which is unilateral in the sense of the local body z-axis.
    
    :param DynamicsFrameTask frame_task: associated frame task
    """
    ...

  def add_unilateral_point_contact(
    self,
    position_task: DynamicsPositionTask, # placo::dynamics::PositionTask
  ) -> PointContact:
    """
    Adds an unilateral point contact, in the sense of the world z-axis.
    
    :param DynamicsPositionTask position_task: the associated position task
    """
    ...

  def clear(
    self,
  ) -> None:
    """
    Clears the internal tasks.
    """
    ...

  def count_contacts(
    arg1: DynamicsSolver,
  ) -> int:
    ...

  damping: float # double
  """
  Global damping that is added to all the joints.
  """

  dt: float # double
  """
  Solver dt (seconds)
  """

  def dump_status(
    self,
  ) -> None:
    """
    Shows the tasks status.
    """
    ...

  def enable_joint_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables/disables joint limits inequalities.
    """
    ...

  def enable_torque_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables/disables torque limits inequalities.
    """
    ...

  def enable_velocity_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables/disables joint velocity inequalities.
    """
    ...

  def enable_velocity_vs_torque_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables the velocity vs torque inequalities.
    """
    ...

  extra_force: numpy.ndarray # Eigen::VectorXd
  """
  Extra force to be added to the system (similar to non-linear terms)
  """

  def get_contact(
    arg1: DynamicsSolver,
    arg2: int,
  ) -> Contact:
    ...

  gravity_only: bool # bool
  """
  Use gravity only (no coriolis, no centrifugal)
  """

  def mask_fbase(
    self,
    masked: bool, # bool
  ) -> None:
    """
    Decides if the floating base should be masked.
    """
    ...

  problem: Problem # placo::problem::Problem
  """
  Instance of the problem.
  """

  def remove_constraint(
    self,
    constraint: DynamicsConstraint, # placo::dynamics::Constraint
  ) -> None:
    """
    Removes a constraint from the solver.
    
    :param DynamicsConstraint constraint: constraint
    """
    ...

  def remove_contact(
    self,
    contact: Contact, # placo::dynamics::Contact
  ) -> None:
    """
    Removes a contact from the solver.
    
    :param Contact contact:
    """
    ...

  def remove_task(
    self,
    task: DynamicsTask, # placo::dynamics::Task
  ) -> None:
    """
    Removes a task from the solver.
    
    :param DynamicsTask task: task
    """
    ...

  robot: RobotWrapper # placo::model::RobotWrapper

  def set_kd(
    self,
    kd: float, # double
  ) -> None:
    """
    Set the kp for all tasks.
    """
    ...

  def set_kp(
    self,
    kp: float, # double
  ) -> None:
    """
    Set the kp for all tasks.
    
    :param float kp:
    """
    ...

  def set_qdd_safe(
    self,
    joint: str, # std::string
    qdd: float, # double
  ) -> None:
    """
    Sets the "safe" Qdd acceptable for a given joint (used by joint limits)
    
    :param str joint: 
    
    :param float qdd:
    """
    ...

  def set_torque_limit(
    self,
    joint: str, # std::string
    limit: float, # double
  ) -> None:
    """
    Sets the allowed torque limit by the solver for a given joint. This will not affect the robot's model effort limit. When computing the velocity vs torque limit, the robot's model effort will still be used. You can see this limit as a continuous limit allowable for the robot, while the robot's model limit is the maximum possible torque.
    
    :param str joint: 
    
    :param float limit:
    """
    ...

  def solve(
    self,
    integrate: bool = False, # bool
  ) -> DynamicsSolverResult:
    ...

  torque_cost: float # double
  """
  Cost for torque regularization (1e-3 by default)
  """


class DynamicsSolverResult:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  qdd: numpy.ndarray # Eigen::VectorXd

  success: bool # bool

  tau: numpy.ndarray # Eigen::VectorXd

  tau_contacts: numpy.ndarray # Eigen::VectorXd

  def tau_dict(
    arg1: DynamicsSolverResult,
    arg2: RobotWrapper,
  ) -> dict:
    ...


class DynamicsTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
  ) -> any:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class DynamicsTorqueTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  A matrix in Ax = b, where x is the accelerations.
  """

  def __init__(
    arg1: object,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  b vector in Ax = b, where x is the accelerations
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  derror: numpy.ndarray # Eigen::MatrixXd
  """
  Current velocity error vector.
  """

  error: numpy.ndarray # Eigen::MatrixXd
  """
  Current error vector.
  """

  kd: float # double
  """
  D gain for position control (if negative, will be critically damped)
  """

  kp: float # double
  """
  K gain for position control.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def reset_torque(
    self,
    joint: str, # std::string
  ) -> None:
    """
    Removes a joint from this task.
    
    :param str joint: joint namle
    """
    ...

  def set_torque(
    self,
    joint: str, # std::string
    torque: float, # double
    kp: float = 0.0, # double
    kd: float = 0.0, # double
  ) -> None:
    """
    Sets the target for a given joint.
    
    :param str joint: joint name 
    
    :param float torque: target torque 
    
    :param float kp: proportional gain (optional) 
    
    :param float kd: derivative gain (optional)
    """
    ...


class Exception:
  def __init__(
    arg1: object,
    arg2: str,
  ) -> None:
    ...

  message: any


class Expression:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Expression A matrix, in Ax + b.
  """

  def Expression(
    self,
  ) -> any:
    ...

  b: numpy.ndarray # Eigen::VectorXd
  """
  Expression b vector, in Ax + b.
  """

  def cols(
    self,
  ) -> int:
    """
    Number of cols in A.
    """
    ...

  @staticmethod
  def from_double(
    self,
    value: float, # const double &
  ) -> Expression:
    """
    Builds an expression from a double (A will be zero, the expression is only one row)
    
    :param float value: value
    """
    ...

  @staticmethod
  def from_vector(
    self,
    v: numpy.ndarray, # const Eigen::VectorXd &
  ) -> Expression:
    """
    Builds an expression from a vector (A will be zeros)
    
    :param numpy.ndarray v: vector
    """
    ...

  def is_constant(
    self,
  ) -> bool:
    """
    checks if the expression is constant (doesn't depend on decision variables)
    """
    ...

  def is_scalar(
    self,
  ) -> bool:
    """
    checks if the expression is a scalar
    """
    ...

  def left_multiply(
    self,
    M: numpy.ndarray, # const Eigen::MatrixXd
  ) -> Expression:
    """
    Multiply an expression on the left by a given matrix M.
    
    :param numpy.ndarray M: matrix
    """
    ...

  def mean(
    self,
  ) -> Expression:
    """
    Reduces a multi-rows expression to the mean of its items.
    """
    ...

  def piecewise_add(
    self,
    f: float, # double
  ) -> Expression:
    """
    Adds the expression element by element to another expression.
    
    :param float f:
    """
    ...

  def rows(
    self,
  ) -> int:
    """
    Number of rows in A.
    """
    ...

  def slice(
    self,
    start: int, # int
    rows: int = -1, # int
  ) -> Expression:
    """
    Slice rows from a given expression.
    
    :param int start: start row 
    
    :param int rows: number of rows (default: -1, all rows)
    """
    ...

  def sum(
    self,
  ) -> Expression:
    """
    Reduces a multi-rows expression to the sum of its items.
    """
    ...

  def value(
    self,
    x: numpy.ndarray, # Eigen::VectorXd
  ) -> numpy.ndarray:
    """
    Retrieve the expression value, given a decision variable. This can be used after a problem is solved to retrieve a specific expression value.
    
    :param numpy.ndarray x:
    """
    ...


class ExternalWrenchContact:
  def ExternalWrenchContact(
    self,
    frame_index: any, # pinocchio::FrameIndex
    reference: any = None, # pinocchio::ReferenceFrame (default: pinocchio::LOCAL_WORLD_ALIGNED)
  ) -> any:
    """
    see DynamicsSolver::add_external_wrench_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  frame_index: any # pinocchio::FrameIndex

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  w_ext: numpy.ndarray # Eigen::VectorXd

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """


class Flags:
  def __init__(
  ) -> any:
    ...

  def as_integer_ratio(
  ) -> any:
    ...

  def bit_count(
  ) -> any:
    ...

  def bit_length(
  ) -> any:
    ...

  collision_as_visual: any

  def conjugate(
  ) -> any:
    ...

  denominator: any

  def from_bytes(
  ) -> any:
    ...

  ignore_collisions: any

  imag: any

  name: any

  names: any

  numerator: any

  real: any

  def to_bytes(
  ) -> any:
    ...

  values: any


class Footstep:
  def Footstep(
    self,
    foot_width: float, # double
    foot_length: float, # double
  ) -> any:
    ...

  foot_length: float # double

  foot_width: float # double

  frame: numpy.ndarray # Eigen::Affine3d

  def overlap(
    self,
    other: Footstep, # placo::humanoid::FootstepsPlanner::Footstep
    margin: float = 0., # double
  ) -> bool:
    ...

  @staticmethod
  def polygon_contains(
    self,
    polygon: list[numpy.ndarray], # std::vector< Eigen::Vector2d > &
    point: numpy.ndarray, # Eigen::Vector2d
  ) -> bool:
    ...

  side: any # placo::humanoid::HumanoidRobot::Side

  def support_polygon(
    self,
  ) -> list[numpy.ndarray]:
    ...


class Footsteps:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def append(
    arg1: Footsteps,
    arg2: object,
  ) -> None:
    ...

  def extend(
    arg1: Footsteps,
    arg2: object,
  ) -> None:
    ...


class FootstepsPlanner:
  def FootstepsPlanner(
    self,
    parameters: HumanoidParameters, # placo::humanoid::HumanoidParameters
  ) -> any:
    """
    Initializes the solver.
    
    :param HumanoidParameters parameters: Parameters of the walk
    """
    ...

  @staticmethod
  def make_supports(
    self,
    footsteps: list[Footstep], # std::vector<placo::humanoid::FootstepsPlanner::Footstep>
    t_start: float, # double
    start: bool = True, # bool
    middle: bool = False, # bool
    end: bool = True, # bool
  ) -> list[Support]:
    """
    Generate the supports from the footsteps.
    
    :param bool start: should we add a double support at the begining of the move? 
    
    :param bool middle: should we add a double support between each step ? 
    
    :param bool end: should we add a double support at the end of the move?
    """
    ...

  def opposite_footstep(
    self,
    footstep: Footstep, # placo::humanoid::FootstepsPlanner::Footstep
    d_x: float = 0., # double
    d_y: float = 0., # double
    d_theta: float = 0., # double
  ) -> Footstep:
    """
    Return the opposite footstep in a neutral position (i.e. at a distance parameters.feet_spacing from the given footstep)
    """
    ...


class FootstepsPlannerNaive:
  def FootstepsPlannerNaive(
    self,
    parameters: HumanoidParameters, # placo::humanoid::HumanoidParameters
  ) -> any:
    ...

  def configure(
    self,
    T_world_left_target: numpy.ndarray, # Eigen::Affine3d
    T_world_right_target: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Configure the naive footsteps planner.
    
    :param numpy.ndarray T_world_left_target: Targetted frame for the left foot 
    
    :param numpy.ndarray T_world_right_target: Targetted frame for the right foot
    """
    ...

  @staticmethod
  def make_supports(
    self,
    footsteps: list[Footstep], # std::vector<placo::humanoid::FootstepsPlanner::Footstep>
    t_start: float, # double
    start: bool = True, # bool
    middle: bool = False, # bool
    end: bool = True, # bool
  ) -> list[Support]:
    """
    Generate the supports from the footsteps.
    
    :param bool start: should we add a double support at the begining of the move? 
    
    :param bool middle: should we add a double support between each step ? 
    
    :param bool end: should we add a double support at the end of the move?
    """
    ...

  def opposite_footstep(
    self,
    footstep: Footstep, # placo::humanoid::FootstepsPlanner::Footstep
    d_x: float = 0., # double
    d_y: float = 0., # double
    d_theta: float = 0., # double
  ) -> Footstep:
    """
    Return the opposite footstep in a neutral position (i.e. at a distance parameters.feet_spacing from the given footstep)
    """
    ...

  def plan(
    self,
    flying_side: any, # placo::humanoid::HumanoidRobot::Side
    T_world_left: numpy.ndarray, # Eigen::Affine3d
    T_world_right: numpy.ndarray, # Eigen::Affine3d
  ) -> list[Footstep]:
    """
    Generate the footsteps.
    
    :param any flying_side: first step side 
    
    :param numpy.ndarray T_world_left: frame of the initial left foot 
    
    :param numpy.ndarray T_world_right: frame of the initial right foot
    """
    ...


class FootstepsPlannerRepetitive:
  def FootstepsPlannerRepetitive(
    self,
    parameters: HumanoidParameters, # placo::humanoid::HumanoidParameters
  ) -> any:
    ...

  def configure(
    self,
    x: float, # double
    y: float, # double
    theta: float, # double
    steps: int, # int
  ) -> None:
    """
    Compute the next footsteps based on coordinates expressed in the support frame laterally translated of +/- feet_spacing.
    
    :param float x: Longitudinal distance 
    
    :param float y: Lateral distance 
    
    :param float theta: Angle 
    
    :param int steps: Number of steps
    """
    ...

  @staticmethod
  def make_supports(
    self,
    footsteps: list[Footstep], # std::vector<placo::humanoid::FootstepsPlanner::Footstep>
    t_start: float, # double
    start: bool = True, # bool
    middle: bool = False, # bool
    end: bool = True, # bool
  ) -> list[Support]:
    """
    Generate the supports from the footsteps.
    
    :param bool start: should we add a double support at the begining of the move? 
    
    :param bool middle: should we add a double support between each step ? 
    
    :param bool end: should we add a double support at the end of the move?
    """
    ...

  def opposite_footstep(
    self,
    footstep: Footstep, # placo::humanoid::FootstepsPlanner::Footstep
    d_x: float = 0., # double
    d_y: float = 0., # double
    d_theta: float = 0., # double
  ) -> Footstep:
    """
    Return the opposite footstep in a neutral position (i.e. at a distance parameters.feet_spacing from the given footstep)
    """
    ...

  def plan(
    self,
    flying_side: any, # placo::humanoid::HumanoidRobot::Side
    T_world_left: numpy.ndarray, # Eigen::Affine3d
    T_world_right: numpy.ndarray, # Eigen::Affine3d
  ) -> list[Footstep]:
    """
    Generate the footsteps.
    
    :param any flying_side: first step side 
    
    :param numpy.ndarray T_world_left: frame of the initial left foot 
    
    :param numpy.ndarray T_world_right: frame of the initial right foot
    """
    ...


class FrameTask:
  T_world_frame: any

  def FrameTask(
    self,
  ) -> any:
    """
    see KinematicsSolver::add_frame_task
    """
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    position_weight: float = 1.0, # double
    orientation_weight: float = 1.0, # double
  ) -> None:
    """
    Configures the frame task.
    
    :param str name: task name 
    
    :param str priority: task priority 
    
    :param float position_weight: weight for the position task 
    
    :param float orientation_weight: weight for the orientation task
    """
    ...

  def orientation(
    arg1: FrameTask,
  ) -> OrientationTask:
    ...

  def position(
    arg1: FrameTask,
  ) -> PositionTask:
    ...


class GearTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def GearTask(
    self,
  ) -> any:
    """
    see KinematicsSolver::add_gear_task
    """
    ...

  def add_gear(
    self,
    target: str, # std::string
    source: str, # std::string
    ratio: float, # double
  ) -> None:
    """
    Adds a gear constraint, you can add multiple source for the same target, they will be summed.
    
    :param str target: target joint 
    
    :param str source: source joint 
    
    :param float ratio: ratio
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def set_gear(
    self,
    target: str, # std::string
    source: str, # std::string
    ratio: float, # double
  ) -> None:
    """
    Sets a gear constraint.
    
    :param str target: target joint 
    
    :param str source: source joint 
    
    :param float ratio: ratio
    """
    ...

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class HumanoidParameters:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  dcm_offset_polygon: list[numpy.ndarray] # std::vector< Eigen::Vector2d >

  def double_support_duration(
    self,
  ) -> float:
    """
    Default duration [s]of a double support.
    """
    ...

  double_support_ratio: float # double
  """
  Duration ratio between single support and double support.
  """

  def double_support_timesteps(
    self,
  ) -> int:
    """
    Default number of timesteps for one double support.
    """
    ...

  def dt(
    self,
  ) -> float:
    """
    Timestep duration for planning [s].
    """
    ...

  def ellipsoid_clip(
    self,
    step: numpy.ndarray, # Eigen::Vector3d
  ) -> numpy.ndarray:
    """
    Applies the ellipsoid clipping to a given step size (dx, dy, dtheta)
    """
    ...

  feet_spacing: float # double
  """
  Lateral spacing between feet [m].
  """

  foot_length: float # double
  """
  Foot length [m].
  """

  foot_width: float # double
  """
  Foot width [m].
  """

  foot_zmp_target_x: float # double
  """
  Target offset for the ZMP x reference trajectory in the foot frame [m].
  """

  foot_zmp_target_y: float # double
  """
  Target offset for the ZMP x reference trajectory in the foot frame, positive is "outward" [m].
  """

  def has_double_support(
    self,
  ) -> bool:
    """
    Checks if the walk resulting from those parameters will have double supports.
    """
    ...

  op_space_polygon: list[numpy.ndarray] # std::vector< Eigen::Vector2d >

  planned_timesteps: int # int
  """
  Planning horizon for the CoM trajectory.
  """

  replan_timesteps: int # int
  """
  Number of timesteps between each replan for the CoM trajectory.
  """

  single_support_duration: float # double
  """
  Single support duration [s].
  """

  single_support_timesteps: int # int
  """
  Number of timesteps for one single support.
  """

  def startend_double_support_duration(
    self,
  ) -> float:
    """
    Default duration [s] of a start/end double support.
    """
    ...

  startend_double_support_ratio: float # double
  """
  Duration ratio between single support and start/end double support.
  """

  def startend_double_support_timesteps(
    self,
  ) -> int:
    """
    Default number of timesteps for one start/end double support.
    """
    ...

  walk_com_height: float # double
  """
  Target CoM height while walking [m].
  """

  walk_dtheta_spacing: float # double
  """
  How much we need to space the feet per dtheta [m/rad].
  """

  walk_foot_height: float # double
  """
  How height the feet are rising while walking [m].
  """

  walk_foot_rise_ratio: float # double
  """
  ratio of time spent at foot height during the step
  """

  walk_max_dtheta: float # double
  """
  Maximum step (yaw)
  """

  walk_max_dx_backward: float # double
  """
  Maximum step (backward)
  """

  walk_max_dx_forward: float # double
  """
  Maximum step (forward)
  """

  walk_max_dy: float # double
  """
  Maximum step (lateral)
  """

  walk_trunk_pitch: float # double
  """
  Trunk pitch while walking [rad].
  """

  zmp_margin: float # double
  """
  Margin for the ZMP to live in the support polygon [m].
  """

  zmp_reference_weight: float # double
  """
  Weight for ZMP reference in the solver.
  """


class HumanoidRobot:
  T_world_support: numpy.ndarray # Eigen::Affine3d
  """
  Transformation from support to world.
  """

  def HumanoidRobot(
    self,
    model_directory: str = "robot", # std::string
    flags: int = 0, # int
    urdf_content: str = "", # std::string
  ) -> any:
    ...

  def add_q_noise(
    self,
    noise: float, # double
  ) -> None:
    """
    Adds some noise to the configuration.
    """
    ...

  def centroidal_map(
    self,
  ) -> numpy.ndarray:
    """
    Centroidal map.
    """
    ...

  collision_model: any # pinocchio::GeometryModel
  """
  Pinocchio collision model.
  """

  def com_jacobian(
    self,
  ) -> numpy.ndarray:
    """
    Jacobian of the CoM position expressed in the world.
    """
    ...

  def com_jacobian_time_variation(
    self,
  ) -> numpy.ndarray:
    """
    Jacobian time variation of the CoM expressed in the world.
    """
    ...

  def com_world(
    self,
  ) -> numpy.ndarray:
    """
    Gets the CoM position in the world.
    """
    ...

  def compute_hessians(
    self,
  ) -> None:
    """
    Compute kinematics hessians.
    """
    ...

  def dcm(
    self,
    com_velocity: numpy.ndarray, # Eigen::Vector2d
    omega: float, # double
  ) -> numpy.ndarray:
    """
    Compute the Divergent Component of Motion (DCM)
    
    :param numpy.ndarray com_velocity: CoM velocity 
    
    :param float omega: Natural frequency of the LIP (= sqrt(g/h))
    """
    ...

  def distances(
    self,
  ) -> list[Distance]:
    """
    Computes all minimum distances between current collision pairs.
    
    :return: <Element 'para' at 0x7f2f0584fb50>
    """
    ...

  def ensure_on_floor(
    self,
  ) -> None:
    """
    Place the robot on its support on the floor.
    """
    ...

  def frame_jacobian(
    self,
    frame: any, # pinocchio::FrameIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Frame jacobian, default reference is LOCAL_WORLD_ALIGNED.
    
    :param any frame: the frame for which we want the jacobian 
    
    :return: <Element 'para' at 0x7f2f057a5800>
    """
    ...

  def frame_jacobian_time_variation(
    self,
    frame: any, # pinocchio::FrameIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Jacobian time variation $\dot J$, default reference is LOCAL_WORLD_ALIGNED.
    
    :param any frame: the frame for which we want the jacobian time variation 
    
    :return: <Element 'para' at 0x7f2f057a6ed0>
    """
    ...

  def frame_names(
    self,
  ) -> list[str]:
    """
    All the frame names.
    """
    ...

  def generalized_gravity(
    self,
  ) -> numpy.ndarray:
    """
    Computes generalized gravity.
    """
    ...

  def get_T_a_b(
    self,
    index_a: any, # pinocchio::FrameIndex
    index_b: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Gets the transformation matrix from frame b to a.
    
    :param any index_a: frame a 
    
    :param any index_b: frame b
    """
    ...

  def get_T_world_fbase(
    self,
  ) -> numpy.ndarray:
    """
    Returns the transformation matrix from the fbase frame (which is the root of the URDF) to the world.
    """
    ...

  def get_T_world_frame(
    self,
    index: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Gets the frame to world transformation matrix for a given frame.
    
    :param any index: frame index
    """
    ...

  def get_T_world_left(
    self,
  ) -> numpy.ndarray:
    ...

  def get_T_world_right(
    self,
  ) -> numpy.ndarray:
    ...

  def get_T_world_trunk(
    self,
  ) -> numpy.ndarray:
    ...

  def get_com_velocity(
    self,
    support: any, # placo::humanoid::HumanoidRobot::Side
    omega_b: numpy.ndarray, # Eigen::Vector3d
  ) -> numpy.ndarray:
    """
    Compute the center of mass velocity from the speed of the motors and the orientation of the trunk.
    
    :param any support: Support side 
    
    :param numpy.ndarray omega_b: Trunk angular velocity in the body frame
    """
    ...

  def get_frame_hessian(
    self,
    frame: any, # pinocchio::FrameIndex
    joint_v_index: int, # int
  ) -> numpy.ndarray:
    """
    Get the component for the hessian of a given frame for a given joint.
    """
    ...

  def get_joint(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Retrieves a joint value from state.q.
    
    :param str name: joint name
    """
    ...

  def get_joint_acceleration(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Gets the joint acceleration from state.qd.
    
    :param str name: joint name
    """
    ...

  def get_joint_offset(
    self,
    name: str, # const std::string &
  ) -> int:
    """
    Gets the offset for a given joint in the state (in State::q)
    
    :param str name: joint name
    """
    ...

  def get_joint_v_offset(
    self,
    name: str, # const std::string &
  ) -> int:
    """
    Gets the offset for a given joint in the state (in State::qd and State::qdd)
    
    :param str name: joint name
    """
    ...

  def get_joint_velocity(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Gets the joint velocity from state.qd.
    
    :param str name: joint name
    """
    ...

  def get_support_side(
    arg1: HumanoidRobot,
  ) -> HumanoidRobot_Side:
    ...

  def get_torques(
    self,
    acc_a: numpy.ndarray, # Eigen::VectorXd
    contact_forces: numpy.ndarray, # Eigen::VectorXd
    use_non_linear_effects: bool = False, # bool
  ) -> numpy.ndarray:
    """
    Compute the torques of the motors from the contact forces.
    
    :param numpy.ndarray acc_a: Accelerations of the actuated DoFs 
    
    :param numpy.ndarray contact_forces: Contact forces from the feet (forces are supposed normal to the ground) 
    
    :param bool use_non_linear_effects: If true, non linear effects are taken into account (state.qd necessary)
    """
    ...

  def get_torques_dict(
    arg1: HumanoidRobot,
    arg2: numpy.ndarray,
    arg3: numpy.ndarray,
    arg4: bool,
  ) -> dict:
    ...

  def integrate(
    self,
    dt: float, # double
  ) -> None:
    """
    Integrates the internal state for a given dt
    
    :param float dt: delta time for integration expressed in seconds
    """
    ...

  def joint_jacobian(
    self,
    joint: any, # pinocchio::JointIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Joint jacobian, default reference is LOCAL_WORLD_ALIGNED.
    """
    ...

  def joint_names(
    self,
    include_floating_base: bool = False, # bool
  ) -> list[str]:
    """
    All the joint names.
    
    :param bool include_floating_base: whether to include the floating base joint (false by default)
    """
    ...

  def load_collision_pairs(
    self,
    filename: str, # const std::string &
  ) -> None:
    """
    Loads collision pairs from a given JSON file.
    
    :param str filename: path to collisions.json file
    """
    ...

  def make_solver(
    arg1: HumanoidRobot,
  ) -> KinematicsSolver:
    ...

  def mass_matrix(
    self,
  ) -> numpy.ndarray:
    """
    Computes the mass matrix.
    """
    ...

  model: any # pinocchio::Model
  """
  Pinocchio model.
  """

  def neutral_state(
    self,
  ) -> RobotWrapper_State:
    """
    builds a neutral state (neutral position, zero speed)
    """
    ...

  def non_linear_effects(
    self,
  ) -> numpy.ndarray:
    """
    Computes non-linear effects (Corriolis, centrifual and gravitationnal effects)
    """
    ...

  @staticmethod
  def other_side(
    self,
    side: any, # placo::humanoid::HumanoidRobot::Side
  ) -> any:
    ...

  def relative_position_jacobian(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Jacobian of the relative position of the position of b expressed in a.
    
    :param any frame_a: frame index A 
    
    :param any frame_b: frame index B
    """
    ...

  def reset(
    self,
  ) -> None:
    """
    Reset internal states, this sets q to the neutral position, qd and qdd to zero.
    """
    ...

  def self_collisions(
    self,
    stop_at_first: bool = False, # bool
  ) -> list[Collision]:
    """
    Finds the self collision in current state, if stop_at_first is true, it will stop at the first collision found.
    
    :param bool stop_at_first: whether to stop at the first collision found 
    
    :return: <Element 'para' at 0x7f2f0584fab0>
    """
    ...

  def set_T_world_fbase(
    self,
    T_world_fbase: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Updates the floating base to match the given transformation matrix.
    
    :param numpy.ndarray T_world_fbase: transformation matrix
    """
    ...

  def set_T_world_frame(
    self,
    frame: any, # pinocchio::FrameIndex
    T_world_frameTarget: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Updates the floating base status so that the given frame has the given transformation matrix.
    
    :param any frame: frame to update 
    
    :param numpy.ndarray T_world_frameTarget: transformation matrix
    """
    ...

  def set_gear_ratio(
    self,
    joint_name: str, # const std::string &
    rotor_gear_ratio: float, # double
  ) -> None:
    """
    Updates the rotor gear ratio (used for apparent inertia computation in the dynamics)
    """
    ...

  def set_gravity(
    self,
    gravity: numpy.ndarray, # Eigen::Vector3d
  ) -> None:
    """
    Sets the gravity vector.
    """
    ...

  def set_joint(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the value of a joint in state.q.
    
    :param str name: joint name 
    
    :param float value: joint value (e.g rad for revolute or meters for prismatic)
    """
    ...

  def set_joint_acceleration(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the joint acceleration in state.qd.
    
    :param str name: joint name 
    
    :param float value: joint acceleration
    """
    ...

  def set_joint_limits(
    self,
    name: str, # const std::string &
    lower: float, # double
    upper: float, # double
  ) -> None:
    """
    Sets the limits for a given joint.
    
    :param str name: joint name 
    
    :param float lower: lower limit 
    
    :param float upper: upper limit
    """
    ...

  def set_joint_velocity(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the joint velocity in state.qd.
    
    :param str name: joint name 
    
    :param float value: joint velocity
    """
    ...

  def set_rotor_inertia(
    self,
    joint_name: str, # const std::string &
    rotor_inertia: float, # double
  ) -> None:
    """
    Updates the rotor inertia (used for apparent inertia computation in the dynamics)
    """
    ...

  def set_torque_limit(
    self,
    name: str, # const std::string &
    limit: float, # double
  ) -> None:
    """
    Sets the torque limit for a given joint.
    
    :param str name: joint name 
    
    :param float limit: torque limit
    """
    ...

  def set_velocity_limit(
    self,
    name: str, # const std::string &
    limit: float, # double
  ) -> None:
    """
    Sets the velocity limit for a given joint.
    
    :param str name: joint name 
    
    :param float limit: joint limit
    """
    ...

  def set_velocity_limits(
    self,
    limit: float, # double
  ) -> None:
    """
    Set the velocity limits for all the joints.
    
    :param float limit: limit
    """
    ...

  state: RobotWrapper_State # placo::model::RobotWrapper::State
  """
  Robot's current state.
  """

  def static_gravity_compensation_torques(
    self,
    frameIndex: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Computes torques needed by the robot to compensate for the generalized gravity, assuming that the given frame is the (only) contact supporting the robot.
    """
    ...

  def static_gravity_compensation_torques_dict(
    arg1: HumanoidRobot,
    arg2: str,
  ) -> dict:
    ...

  support_is_both: bool # bool
  """
  Are both feet supporting the robot.
  """

  def torques_from_acceleration_with_fixed_frame(
    self,
    qdd_a: numpy.ndarray, # Eigen::VectorXd
    frameIndex: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Computes required torques in the robot DOFs for a given acceleration of the actuated DOFs, assuming that the given frame is fixed.
    
    :param numpy.ndarray qdd_a: acceleration of the actuated DOFs
    """
    ...

  def torques_from_acceleration_with_fixed_frame_dict(
    self: HumanoidRobot,
    qdd_a: numpy.ndarray,
    frame: str,
  ) -> dict:
    """
    Computes the torque required to reach given acceleration in fixed frame
    """
    ...

  def total_mass(
    self,
  ) -> float:
    """
    Total mass.
    """
    ...

  def update_kinematics(
    self,
  ) -> None:
    """
    Update internal computation for kinematics (frames, jacobian). This method should be called when the robot state has changed.
    """
    ...

  def update_support_side(
    self,
    new_side: any, # placo::humanoid::HumanoidRobot::Side
  ) -> None:
    """
    Updates which frame should be the current support.
    """
    ...

  visual_model: any # pinocchio::GeometryModel
  """
  Pinocchio visual model.
  """

  def zmp(
    self,
    com_acceleration: numpy.ndarray, # Eigen::Vector2d
    omega: float, # double
  ) -> numpy.ndarray:
    """
    Compute the Zero-tilting Moment Point (ZMP)
    
    :param numpy.ndarray com_acceleration: CoM acceleration 
    
    :param float omega: Natural frequency of the LIP (= sqrt(g/h))
    """
    ...


class HumanoidRobot_Side:
  def __init__(
  ) -> any:
    ...

  def as_integer_ratio(
  ) -> any:
    ...

  def bit_count(
  ) -> any:
    ...

  def bit_length(
  ) -> any:
    ...

  def conjugate(
  ) -> any:
    ...

  denominator: any

  def from_bytes(
  ) -> any:
    ...

  imag: any

  left: any

  name: any

  names: any

  numerator: any

  real: any

  right: any

  def to_bytes(
  ) -> any:
    ...

  values: any


class Integrator:
  """
  Integrator can be used to efficiently build expressions and values over a decision variable that is integrated over time with a given linear system.
  """
  A: numpy.ndarray # Eigen::MatrixXd
  """
  The discrete system matrix such that $X_{k+1} = A X_k + B u_k$.
  """

  B: numpy.ndarray # Eigen::MatrixXd
  """
  The discrete system matrix such that $X_{k+1} = A X_k + B u_k$.
  """

  M: numpy.ndarray # Eigen::MatrixXd
  """
  The continuous system matrix.
  """

  def Integrator(
    self,
  ) -> any:
    ...

  def expr(
    self,
    step: int, # int
    diff: int = -1, # int
  ) -> Expression:
    """
    Builds an expression for the given step and differentiation.
    
    :param int step: the step, (if -1 the last step will be used) 
    
    :param int diff: differentiation (if -1, the expression will be a vector of size order with all orders)
    """
    ...

  def expr_t(
    self,
    t: float, # double
    diff: int = -1, # int
  ) -> Expression:
    """
    Builds an expression for the given time and differentiation.
    
    :param float t: the time 
    
    :param int diff: differentiation (if -1, the expression will be a vector of size order with all orders)
    """
    ...

  final_transition_matrix: numpy.ndarray # Eigen::MatrixXd
  """
  Caching the discrete matrix for the last step.
  """

  def get_trajectory(
    self,
  ) -> IntegratorTrajectory:
    """
    Retrieve a trajectory after a solve.
    """
    ...

  t_start: float # double
  """
  Time offset for the trajectory.
  """

  @staticmethod
  def upper_shift_matrix(
    self,
    order: int, # int
  ) -> numpy.ndarray:
    """
    Builds a matrix M so that the system differential equation is dX = M X.
    """
    ...

  def value(
    self,
    t: float, # double
    diff: int, # int
  ) -> float:
    """
    Computes.
    
    :param float t: 
    
    :param int diff:
    """
    ...


class IntegratorTrajectory:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def duration(
    self,
  ) -> float:
    """
    Trajectory duration.
    """
    ...

  def value(
    self,
    t: float, # double
    diff: int, # int
  ) -> float:
    """
    Gets the value of the trajectory at a given time and differentiation.
    
    :param float t: time 
    
    :param int diff: differentiation
    """
    ...


class JointSpaceHalfSpacesConstraint:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in Aq <= b.
  """

  def JointSpaceHalfSpacesConstraint(
    self,
    A: numpy.ndarray, # const Eigen::MatrixXd
    b: numpy.ndarray, # Eigen::VectorXd
  ) -> any:
    """
    Ensures that, in joint-space we have Aq <= b Note that the floating base terms will be ignored in A. However, A should still be of dimension n_constraints x n_q.
    """
    ...

  b: numpy.ndarray # Eigen::VectorXd
  """
  Vector b in Aq <= b.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class JointsTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def JointsTask(
    self,
  ) -> any:
    """
    see KinematicsSolver::add_joints_task
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  def get_joint(
    self,
    joint: str, # std::string
  ) -> float:
    """
    Returns the target value of a joint.
    
    :param str joint: joint
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def set_joint(
    self,
    joint: str, # std::string
    target: float, # double
  ) -> None:
    """
    Sets a joint target.
    
    :param str joint: joint 
    
    :param float target: target value
    """
    ...

  def set_joints(
    arg1: JointsTask,
    arg2: dict,
  ) -> None:
    ...

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class KinematicsConstraint:
  def __init__(
  ) -> any:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class KinematicsSolver:
  N: int # int
  """
  Size of the problem (number of variables)
  """

  def KinematicsSolver(
    self,
    robot_: RobotWrapper, # placo::model::RobotWrapper
  ) -> any:
    ...

  def add_avoid_self_collisions_constraint(
    self,
  ) -> AvoidSelfCollisionsKinematicsConstraint:
    """
    Adds a self collision avoidance constraint.
    """
    ...

  def add_axisalign_task(
    self,
    frame: any, # pinocchio::FrameIndex
    axis_frame: numpy.ndarray, # Eigen::Vector3d
    targetAxis_world: numpy.ndarray, # Eigen::Vector3d
  ) -> AxisAlignTask:
    """
    Adds an axis alignment task. The goal here is to keep the given axis (expressed in the given frame) aligned with another one (given in the world)
    
    :param any frame: the robot frame we want to control 
    
    :param numpy.ndarray axis_frame: the axis to align, expressed in the robot frame 
    
    :param numpy.ndarray targetAxis_world: the target axis (in the world) we want to be aligned with
    """
    ...

  def add_centroidal_momentum_task(
    self,
    L_world: numpy.ndarray, # Eigen::Vector3d
  ) -> CentroidalMomentumTask:
    """
    Adding a centroidal momentum task.
    
    :param numpy.ndarray L_world: desired centroidal angular momentum in the world
    """
    ...

  def add_com_polygon_constraint(
    self,
    polygon: list[numpy.ndarray], # std::vector< Eigen::Vector2d >
    margin: float = 0., # double
  ) -> CoMPolygonConstraint:
    """
    Adds a CoM polygon constraint.
    
    :param list[numpy.ndarray] polygon: clockwise polygon 
    
    :param float margin: margin
    """
    ...

  def add_com_task(
    self,
    targetCom_world: numpy.ndarray, # Eigen::Vector3d
  ) -> CoMTask:
    """
    Adds a com position task.
    
    :param numpy.ndarray targetCom_world: the target position, expressed in the world (as T_world_frame)
    """
    ...

  def add_cone_constraint(
    self,
    frame_a: str, # std::string
    frame_b: str, # std::string
    alpha_max: float, # double
  ) -> ConeConstraint:
    """
    Adds a Cone constraint.
    
    :param str frame_a: frame A 
    
    :param str frame_b: frame B 
    
    :param float alpha_max: alpha max (in radians) between the frame z-axis and the cone frame zt-axis
    """
    ...

  def add_constraint(
    self,
    constraint: KinematicsConstraint, # placo::kinematics::Constraint
  ) -> None:
    """
    Adds a custom constraint to the solver.
    
    :param KinematicsConstraint constraint:
    """
    ...

  def add_distance_task(
    self,
    frame_a: str, # std::string
    frame_b: str, # std::string
    distance: float, # double
  ) -> DistanceTask:
    """
    Adds a distance task to be maintained between two frames.
    
    :param str frame_a: frame a 
    
    :param str frame_b: frame b 
    
    :param float distance: distance to maintain
    """
    ...

  def add_frame_task(
    self,
    frame: str, # std::string
    T_world_frame: numpy.ndarray = None, # Eigen::Affine3d (default: Eigen::Affine3d::Identity())
  ) -> FrameTask:
    """
    Adds a frame task, this is equivalent to a position + orientation task, resulting in decoupled tasks for a given frame.
    
    :param str frame: the robot frame we want to control 
    
    :param numpy.ndarray T_world_frame: the target for the frame we want to control, expressed in the world (as T_world_frame)
    """
    ...

  def add_gear_task(
    self,
  ) -> GearTask:
    """
    Adds a gear task, allowing replication of joints.
    """
    ...

  def add_joint_space_half_spaces_constraint(
    self,
    A: numpy.ndarray, # Eigen::MatrixXd
    b: numpy.ndarray, # Eigen::VectorXd
  ) -> JointSpaceHalfSpacesConstraint:
    """
    Adds a joint-space half-spaces constraint, such that Aq <= b.
    
    :param numpy.ndarray A: matrix A in Aq <= b 
    
    :param numpy.ndarray b: vector b in Aq <= b
    """
    ...

  def add_joints_task(
    self,
    joints: dict[str, float], # std::map< std::string, double > &
  ) -> JointsTask:
    """
    Adds joints task.
    
    :param dict[str, float] joints: value for the joints
    """
    ...

  def add_kinetic_energy_regularization_task(
    self,
    magnitude: float = 1e-6, # double
  ) -> KineticEnergyRegularizationTask:
    """
    Adds a kinetic energy regularization task for a given magnitude.
    
    :param float magnitude: regularization magnitude
    """
    ...

  def add_manipulability_task(
    self,
    frame: any, # pinocchio::FrameIndex
    type: any, # placo::kinematics::ManipulabilityTask::Type
    lambda: float = 1.0, # double
  ) -> ManipulabilityTask:
    """
    Adds a manipulability regularization task for a given magnitude.
    """
    ...

  def add_orientation_task(
    self,
    frame: str, # std::string
    R_world_frame: numpy.ndarray, # Eigen::Matrix3d
  ) -> OrientationTask:
    """
    Adds an orientation task.
    
    :param str frame: the robot frame we want to control 
    
    :param numpy.ndarray R_world_frame: the target orientation we want to achieve, expressed in the world (as T_world_frame)
    """
    ...

  def add_position_task(
    self,
    frame: str, # std::string
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> PositionTask:
    """
    Adds a position task.
    
    :param str frame: the robot frame we want to control 
    
    :param numpy.ndarray target_world: the target position, expressed in the world (as T_world_frame)
    """
    ...

  def add_regularization_task(
    self,
    magnitude: float = 1e-6, # double
  ) -> RegularizationTask:
    """
    Adds a regularization task for a given magnitude.
    
    :param float magnitude: regularization magnitude
    """
    ...

  def add_relative_frame_task(
    self,
    frame_a: str, # std::string
    frame_b: str, # std::string
    T_a_b: numpy.ndarray, # Eigen::Affine3d
  ) -> RelativeFrameTask:
    """
    Adds a relative frame task.
    
    :param str frame_a: frame a 
    
    :param str frame_b: frame b 
    
    :param numpy.ndarray T_a_b: desired transformation
    """
    ...

  def add_relative_orientation_task(
    self,
    frame_a: str, # std::string
    frame_b: str, # std::string
    R_a_b: numpy.ndarray, # Eigen::Matrix3d
  ) -> RelativeOrientationTask:
    """
    Adds a relative orientation task.
    
    :param str frame_a: frame a 
    
    :param str frame_b: frame b 
    
    :param numpy.ndarray R_a_b: the desired orientation
    """
    ...

  def add_relative_position_task(
    self,
    frame_a: str, # std::string
    frame_b: str, # std::string
    target: numpy.ndarray, # Eigen::Vector3d
  ) -> RelativePositionTask:
    """
    Adds a relative position task.
    
    :param str frame_a: frame a 
    
    :param str frame_b: frame b 
    
    :param numpy.ndarray target: the target vector between frame a and b (expressed in world)
    """
    ...

  def add_task(
    self,
    task: Task, # placo::kinematics::Task
  ) -> None:
    """
    Adds a custom task to the solver.
    
    :param Task task:
    """
    ...

  def add_wheel_task(
    self,
    joint: str, # const std::string
    radius: float, # double
    omniwheel: bool = False, # bool
  ) -> WheelTask:
    """
    Adds a wheel task.
    
    :param str joint: joint name 
    
    :param float radius: wheel radius 
    
    :param bool omniwheel: true if it's an omniwheel (can slide laterally)
    """
    ...

  def clear(
    self,
  ) -> None:
    """
    Clears the internal tasks.
    """
    ...

  dt: float # double
  """
  solver dt (for speeds limiting)
  """

  def dump_status(
    self,
  ) -> None:
    """
    Shows the tasks status.
    """
    ...

  def enable_joint_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables/disables joint limits inequalities.
    """
    ...

  def enable_velocity_limits(
    self,
    enable: bool, # bool
  ) -> None:
    """
    Enables/disables joint velocity inequalities.
    """
    ...

  def mask_dof(
    self,
    dof: str, # std::string
  ) -> None:
    """
    Masks (disables a DoF) from being used by the QP solver (it can't provide speed)
    
    :param str dof: the dof name
    """
    ...

  def mask_fbase(
    self,
    masked: bool, # bool
  ) -> None:
    """
    Decides if the floating base should be masked.
    """
    ...

  problem: Problem # placo::problem::Problem
  """
  The underlying QP problem.
  """

  def remove_constraint(
    self,
    constraint: KinematicsConstraint, # placo::kinematics::Constraint
  ) -> None:
    """
    Removes aconstraint from the solver.
    
    :param KinematicsConstraint constraint: constraint
    """
    ...

  def remove_task(
    self,
    task: Task, # placo::kinematics::Task
  ) -> None:
    """
    Removes a task from the solver.
    
    :param Task task: task
    """
    ...

  robot: RobotWrapper # placo::model::RobotWrapper
  """
  The robot controlled by this solver.
  """

  scale: float # double
  """
  scale obtained when using tasks scaling
  """

  def solve(
    self,
    apply: bool = False, # bool
  ) -> numpy.ndarray:
    """
    Constructs the QP problem and solves it.
    
    :param bool apply: apply the solution to the robot model
    """
    ...

  def tasks_count(
    self,
  ) -> int:
    """
    Number of tasks.
    """
    ...

  def unmask_dof(
    self,
    dof: str, # std::string
  ) -> None:
    """
    Unmsks (enables a DoF) from being used by the QP solver (it can provide speed)
    
    :param str dof: the dof name
    """
    ...


class KineticEnergyRegularizationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def __init__(
    arg1: object,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class LIPM:
  """
  LIPM is an helper that can be used to build problem involving LIPM dynamics. The decision variables introduced here are jerks, which is piecewise constant.
  """
  def LIPM(
    self,
  ) -> any:
    ...

  def acc(
    self,
    timestep: int, # int
  ) -> Expression:
    ...

  @staticmethod
  def build_LIPM_from_previous(
    self,
    problem: Problem, # placo::problem::Problem
    dt: float, # double
    timesteps: int, # int
    t_start: float, # double
    previous: LIPM, # placo::humanoid::LIPM
  ) -> LIPM:
    ...

  @staticmethod
  def compute_omega(
    self,
    com_height: float, # double
  ) -> float:
    """
    Compute the natural frequency of a LIPM given its height (omega = sqrt(g / h))
    """
    ...

  def dcm(
    self,
    timestep: int, # int
    omega: float, # double
  ) -> Expression:
    ...

  dt: float # double

  def dzmp(
    self,
    timestep: int, # int
    omega_2: float, # double
  ) -> Expression:
    ...

  def get_trajectory(
    self,
  ) -> LIPMTrajectory:
    """
    Get the LIPM trajectory. Should be used after solving the problem.
    """
    ...

  def jerk(
    self,
    timestep: int, # int
  ) -> Expression:
    ...

  def pos(
    self,
    timestep: int, # int
  ) -> Expression:
    ...

  t_end: any

  t_start: float # double

  timesteps: int # int

  def vel(
    self,
    timestep: int, # int
  ) -> Expression:
    ...

  x: Integrator # placo::problem::Integrator

  x_var: Variable # placo::problem::Variable

  y: Integrator # placo::problem::Integrator

  y_var: Variable # placo::problem::Variable

  def zmp(
    self,
    timestep: int, # int
    omega_2: float, # double
  ) -> Expression:
    ...


class LIPMTrajectory:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def acc(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def dcm(
    self,
    t: float, # double
    omega: float, # double
  ) -> numpy.ndarray:
    ...

  def dzmp(
    self,
    t: float, # double
    omega_2: float, # double
  ) -> numpy.ndarray:
    ...

  def jerk(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def pos(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def vel(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def zmp(
    self,
    t: float, # double
    omega_2: float, # double
  ) -> numpy.ndarray:
    ...


class LineContact:
  R_world_surface: numpy.ndarray # Eigen::Matrix3d
  """
  rotation matrix expressing the surface frame in the world frame (for unilateral contact)
  """

  def LineContact(
    self,
    frame_task: DynamicsFrameTask, # placo::dynamics::FrameTask
    unilateral: bool, # bool
  ) -> any:
    """
    see DynamicsSolver::add_fixed_planar_contact and DynamicsSolver::add_unilateral_planar_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  length: float # double
  """
  Rectangular contact length along local x-axis.
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  def orientation_task(
    arg1: LineContact,
  ) -> DynamicsOrientationTask:
    ...

  def position_task(
    arg1: LineContact,
  ) -> DynamicsPositionTask:
    ...

  unilateral: bool # bool
  """
  true for unilateral contact with the ground
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """

  def zmp(
    self,
  ) -> numpy.ndarray:
    """
    Returns the contact ZMP in the local frame.
    """
    ...


class ManipulabilityTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def ManipulabilityTask(
    self,
    frame_index: any, # pinocchio::FrameIndex
    type: any, # placo::kinematics::ManipulabilityTask::Type
    lambda_: float = 1.0, # double
  ) -> any:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  lambda_: any

  manipulability: float # double
  """
  The last computed manipulability value.
  """

  minimize: bool # bool
  """
  Should the manipulability be minimized (can be useful to find singularities)
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class OrientationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  R_world_frame: numpy.ndarray # Eigen::Matrix3d
  """
  Target frame orientation in the world.
  """

  def OrientationTask(
    self,
    frame_index: any, # pinocchio::FrameIndex
    R_world_frame: numpy.ndarray, # Eigen::Matrix3d
  ) -> any:
    """
    See KinematicsSolver::add_orientation_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_index: any # pinocchio::FrameIndex
  """
  Frame.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class PointContact:
  R_world_surface: numpy.ndarray # Eigen::Matrix3d
  """
  rotation matrix expressing the surface frame in the world frame (for unilateral contact)
  """

  def PointContact(
    self,
    position_task: DynamicsPositionTask, # placo::dynamics::PositionTask
    unilateral: bool, # bool
  ) -> any:
    """
    see DynamicsSolver::add_point_contact and DynamicsSolver::add_unilateral_point_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  def position_task(
    arg1: PointContact,
  ) -> DynamicsPositionTask:
    ...

  unilateral: bool # bool
  """
  true for unilateral contact with the ground
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """


class PolygonConstraint:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  @staticmethod
  def in_polygon(
    self,
    expression_x: Expression, # placo::problem::Expression
    expression_y: Expression, # placo::problem::Expression
    polygon: list[numpy.ndarray], # std::vector< Eigen::Vector2d >
    margin: float = 0., # double
  ) -> ProblemConstraint:
    ...

  @staticmethod
  def in_polygon_xy(
    self,
    expression_xy: Expression, # placo::problem::Expression
    polygon: list[numpy.ndarray], # std::vector< Eigen::Vector2d >
    margin: float = 0., # double
  ) -> ProblemConstraint:
    """
    Given a polygon, produces inequalities so that the given point lies inside the polygon. WARNING: Polygon must be clockwise (meaning that the exterior of the shape is on the trigonometric normal of the vertices)
    """
    ...


class Polynom:
  def Polynom(
    self,
    coefficients: numpy.ndarray, # Eigen::VectorXd
  ) -> any:
    ...

  coefficients: numpy.ndarray # Eigen::VectorXd
  """
  coefficients, from highest to lowest
  """

  @staticmethod
  def derivative_coefficient(
    self,
    degree: int, # int
    derivative: int, # int
  ) -> int:
    """
    Computes the coefficient in front of term of degree degree after derivative differentiations.
    
    :param int degree: degree 
    
    :param int derivative: number of differentiations
    """
    ...

  def value(
    self,
    x: float, # double
    derivative: int = 0, # int
  ) -> float:
    """
    Computes the value of polynom.
    
    :param float x: abscissa 
    
    :param int derivative: differentiation order (0: p, 1: p', 2: p'' etc.)
    """
    ...


class PositionTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def PositionTask(
    self,
    frame_index: any, # pinocchio::FrameIndex
    target_world: numpy.ndarray, # Eigen::Vector3d
  ) -> any:
    """
    See KinematicsSolver::add_position_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_index: any # pinocchio::FrameIndex
  """
  Frame.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target_world: numpy.ndarray # Eigen::Vector3d
  """
  Target position in the world.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class Prioritized:
  def Prioritized(
    self,
  ) -> any:
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """


class Problem:
  def Problem(
    self,
  ) -> any:
    ...

  def add_constraint(
    self,
    constraint: ProblemConstraint, # placo::problem::ProblemConstraint
  ) -> ProblemConstraint:
    """
    Adds a given constraint to the problem.
    
    :param ProblemConstraint constraint:
    """
    ...

  def add_limit(
    self,
    expression: Expression, # placo::problem::Expression
    target: numpy.ndarray, # Eigen::VectorXd
  ) -> ProblemConstraint:
    """
    Adds a limit, "absolute" inequality constraint (abs(Ax + b) <= t)
    
    :param Expression expression: 
    
    :param numpy.ndarray target:
    """
    ...

  def add_variable(
    self,
    size: int = 1, # int
  ) -> Variable:
    """
    Adds a n-dimensional variable to a problem.
    
    :param int size: dimension of the variable
    """
    ...

  def clear_constraints(
    self,
  ) -> None:
    """
    Clear all the constraints.
    """
    ...

  def clear_variables(
    self,
  ) -> None:
    """
    Clear all the variables.
    """
    ...

  determined_variables: int # int
  """
  Number of determined variables.
  """

  def dump_status(
    self,
  ) -> None:
    ...

  free_variables: int # int
  """
  Number of free variables to solve.
  """

  n_equalities: int # int
  """
  Number of equalities.
  """

  n_inequalities: int # int
  """
  Number of inequality constraints.
  """

  n_variables: int # int
  """
  Number of problem variables that need to be solved.
  """

  regularization: float # double
  """
  Default internal regularization.
  """

  rewrite_equalities: bool # bool
  """
  If set to true, a QR factorization will be performed on the equality constraints, and the QP will be called with free variables only.
  """

  slack_variables: int # int
  """
  Number of slack variables in the solver.
  """

  slacks: numpy.ndarray # Eigen::VectorXd
  """
  Computed slack variables.
  """

  def solve(
    self,
  ) -> None:
    """
    Solves the problem, raises QPError in case of failure.
    """
    ...

  use_sparsity: bool # bool
  """
  If set to true, some sparsity optimizations will be performed when building the problem Hessian. This optimization is generally not useful for small problems.
  """

  x: numpy.ndarray # Eigen::VectorXd
  """
  Computed result.
  """


class ProblemConstraint:
  """
  Represents a constraint to be enforced by a Problem.
  """
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def configure(
    self,
    type: str, # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the constraint.
    
    :param float weight: weight
    """
    ...

  expression: Expression # placo::problem::Expression
  """
  The constraint expression (Ax + b)
  """

  is_active: bool # bool
  """
  This flag will be set by the solver if the constraint is active in the optimal solution.
  """

  priority: any # placo::problem::ProblemConstraint::Priority
  """
  Constraint priority.
  """

  weight: float # double
  """
  Constraint weight (for soft constraints)
  """


class ProblemPolynom:
  def ProblemPolynom(
    self,
    variable: Variable, # placo::problem::Variable
  ) -> any:
    ...

  def expr(
    self,
    x: float, # double
    derivative: int = 0, # int
  ) -> Expression:
    """
    Builds a problem expression for the value of the polynom.
    
    :param float x: abscissa 
    
    :param int derivative: differentiation order (0: p, 1: p', 2: p'' etc.)
    """
    ...

  def get_polynom(
    self,
  ) -> Polynom:
    """
    Obtain resulting polynom (after problem is solved)
    """
    ...


class PuppetContact:
  def PuppetContact(
    self,
  ) -> any:
    """
    see DynamicsSolver::add_puppet_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """


class QPError:
  """
  Exception raised by Problem in case of failure.
  """
  def QPError(
    self,
    message: str = "", # std::string
  ) -> any:
    ...

  def what(
    arg1: QPError,
  ) -> str:
    ...


class RegularizationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def __init__(
    arg1: object,
  ) -> None:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class RelativeFrameTask:
  T_a_b: any

  def RelativeFrameTask(
    self,
    position: RelativePositionTask, # placo::kinematics::RelativePositionTask
    orientation: RelativeOrientationTask, # placo::kinematics::RelativeOrientationTask
  ) -> any:
    """
    see KinematicsSolver::add_relative_frame_task
    """
    ...

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    position_weight: float = 1.0, # double
    orientation_weight: float = 1.0, # double
  ) -> None:
    """
    Configures the relative frame task.
    
    :param str name: task name 
    
    :param str priority: task priority 
    
    :param float position_weight: weight for the position task 
    
    :param float orientation_weight: weight for the orientation task
    """
    ...

  def orientation(
    arg1: RelativeFrameTask,
  ) -> RelativeOrientationTask:
    ...

  def position(
    arg1: RelativeFrameTask,
  ) -> RelativePositionTask:
    ...


class RelativeOrientationTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  R_a_b: numpy.ndarray # Eigen::Matrix3d
  """
  Target relative orientation of b in a.
  """

  def RelativeOrientationTask(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
    R_a_b: numpy.ndarray, # Eigen::Matrix3d
  ) -> any:
    """
    See KinematicsSolver::add_relative_orientation_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_a: any # pinocchio::FrameIndex
  """
  Frame A.
  """

  frame_b: any # pinocchio::FrameIndex
  """
  Frame B.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class RelativePositionTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def RelativePositionTask(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
    target: numpy.ndarray, # Eigen::Vector3d
  ) -> any:
    """
    See KinematicsSolver::add_relative_position_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  frame_a: any # pinocchio::FrameIndex
  """
  Frame A.
  """

  frame_b: any # pinocchio::FrameIndex
  """
  Frame B.
  """

  mask: AxisesMask # placo::tools::AxisesMask
  """
  Mask.
  """

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  target: numpy.ndarray # Eigen::Vector3d
  """
  Target position of B in A.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class RobotWrapper:
  def RobotWrapper(
    self,
    model_directory: str, # std::string
    flags: int = 0, # int
    urdf_content: str = "", # std::string
  ) -> any:
    """
    Creates a robot wrapper from a URDF file.
    
    :param str model_directory: robot model (URDF). It can be a path to an URDF file, or a directory containing an URDF file named 'robot.urdf' 
    
    :param int flags: see Flags 
    
    :param str urdf_content: if it is not empty, it will be used as the URDF content instead of loading it from the file
    """
    ...

  def add_q_noise(
    self,
    noise: float, # double
  ) -> None:
    """
    Adds some noise to the configuration.
    """
    ...

  def centroidal_map(
    self,
  ) -> numpy.ndarray:
    """
    Centroidal map.
    """
    ...

  collision_model: any # pinocchio::GeometryModel
  """
  Pinocchio collision model.
  """

  def com_jacobian(
    self,
  ) -> numpy.ndarray:
    """
    Jacobian of the CoM position expressed in the world.
    """
    ...

  def com_jacobian_time_variation(
    self,
  ) -> numpy.ndarray:
    """
    Jacobian time variation of the CoM expressed in the world.
    """
    ...

  def com_world(
    self,
  ) -> numpy.ndarray:
    """
    Gets the CoM position in the world.
    """
    ...

  def compute_hessians(
    self,
  ) -> None:
    """
    Compute kinematics hessians.
    """
    ...

  def distances(
    self,
  ) -> list[Distance]:
    """
    Computes all minimum distances between current collision pairs.
    
    :return: <Element 'para' at 0x7f2f0573cf40>
    """
    ...

  def frame_jacobian(
    self,
    frame: any, # pinocchio::FrameIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Frame jacobian, default reference is LOCAL_WORLD_ALIGNED.
    
    :param any frame: the frame for which we want the jacobian 
    
    :return: <Element 'para' at 0x7f2f0573c6d0>
    """
    ...

  def frame_jacobian_time_variation(
    self,
    frame: any, # pinocchio::FrameIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Jacobian time variation $\dot J$, default reference is LOCAL_WORLD_ALIGNED.
    
    :param any frame: the frame for which we want the jacobian time variation 
    
    :return: <Element 'para' at 0x7f2f058daca0>
    """
    ...

  def frame_names(
    self,
  ) -> list[str]:
    """
    All the frame names.
    """
    ...

  def generalized_gravity(
    self,
  ) -> numpy.ndarray:
    """
    Computes generalized gravity.
    """
    ...

  def get_T_a_b(
    self,
    index_a: any, # pinocchio::FrameIndex
    index_b: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Gets the transformation matrix from frame b to a.
    
    :param any index_a: frame a 
    
    :param any index_b: frame b
    """
    ...

  def get_T_world_fbase(
    self,
  ) -> numpy.ndarray:
    """
    Returns the transformation matrix from the fbase frame (which is the root of the URDF) to the world.
    """
    ...

  def get_T_world_frame(
    self,
    index: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Gets the frame to world transformation matrix for a given frame.
    
    :param any index: frame index
    """
    ...

  def get_frame_hessian(
    self,
    frame: any, # pinocchio::FrameIndex
    joint_v_index: int, # int
  ) -> numpy.ndarray:
    """
    Get the component for the hessian of a given frame for a given joint.
    """
    ...

  def get_joint(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Retrieves a joint value from state.q.
    
    :param str name: joint name
    """
    ...

  def get_joint_acceleration(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Gets the joint acceleration from state.qd.
    
    :param str name: joint name
    """
    ...

  def get_joint_offset(
    self,
    name: str, # const std::string &
  ) -> int:
    """
    Gets the offset for a given joint in the state (in State::q)
    
    :param str name: joint name
    """
    ...

  def get_joint_v_offset(
    self,
    name: str, # const std::string &
  ) -> int:
    """
    Gets the offset for a given joint in the state (in State::qd and State::qdd)
    
    :param str name: joint name
    """
    ...

  def get_joint_velocity(
    self,
    name: str, # const std::string &
  ) -> float:
    """
    Gets the joint velocity from state.qd.
    
    :param str name: joint name
    """
    ...

  def integrate(
    self,
    dt: float, # double
  ) -> None:
    """
    Integrates the internal state for a given dt
    
    :param float dt: delta time for integration expressed in seconds
    """
    ...

  def joint_jacobian(
    self,
    joint: any, # pinocchio::JointIndex
    ref: any = None, # pinocchio::ReferenceFrame (default: pinocchio::ReferenceFrame::LOCAL_WORLD_ALIGNED)
  ) -> numpy.ndarray:
    """
    Joint jacobian, default reference is LOCAL_WORLD_ALIGNED.
    """
    ...

  def joint_names(
    self,
    include_floating_base: bool = False, # bool
  ) -> list[str]:
    """
    All the joint names.
    
    :param bool include_floating_base: whether to include the floating base joint (false by default)
    """
    ...

  def load_collision_pairs(
    self,
    filename: str, # const std::string &
  ) -> None:
    """
    Loads collision pairs from a given JSON file.
    
    :param str filename: path to collisions.json file
    """
    ...

  def make_solver(
    arg1: RobotWrapper,
  ) -> KinematicsSolver:
    ...

  def mass_matrix(
    self,
  ) -> numpy.ndarray:
    """
    Computes the mass matrix.
    """
    ...

  model: any # pinocchio::Model
  """
  Pinocchio model.
  """

  def neutral_state(
    self,
  ) -> RobotWrapper_State:
    """
    builds a neutral state (neutral position, zero speed)
    """
    ...

  def non_linear_effects(
    self,
  ) -> numpy.ndarray:
    """
    Computes non-linear effects (Corriolis, centrifual and gravitationnal effects)
    """
    ...

  def relative_position_jacobian(
    self,
    frame_a: any, # pinocchio::FrameIndex
    frame_b: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Jacobian of the relative position of the position of b expressed in a.
    
    :param any frame_a: frame index A 
    
    :param any frame_b: frame index B
    """
    ...

  def reset(
    self,
  ) -> None:
    """
    Reset internal states, this sets q to the neutral position, qd and qdd to zero.
    """
    ...

  def self_collisions(
    self,
    stop_at_first: bool = False, # bool
  ) -> list[Collision]:
    """
    Finds the self collision in current state, if stop_at_first is true, it will stop at the first collision found.
    
    :param bool stop_at_first: whether to stop at the first collision found 
    
    :return: <Element 'para' at 0x7f2f0573d300>
    """
    ...

  def set_T_world_fbase(
    self,
    T_world_fbase: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Updates the floating base to match the given transformation matrix.
    
    :param numpy.ndarray T_world_fbase: transformation matrix
    """
    ...

  def set_T_world_frame(
    self,
    frame: any, # pinocchio::FrameIndex
    T_world_frameTarget: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Updates the floating base status so that the given frame has the given transformation matrix.
    
    :param any frame: frame to update 
    
    :param numpy.ndarray T_world_frameTarget: transformation matrix
    """
    ...

  def set_gear_ratio(
    self,
    joint_name: str, # const std::string &
    rotor_gear_ratio: float, # double
  ) -> None:
    """
    Updates the rotor gear ratio (used for apparent inertia computation in the dynamics)
    """
    ...

  def set_gravity(
    self,
    gravity: numpy.ndarray, # Eigen::Vector3d
  ) -> None:
    """
    Sets the gravity vector.
    """
    ...

  def set_joint(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the value of a joint in state.q.
    
    :param str name: joint name 
    
    :param float value: joint value (e.g rad for revolute or meters for prismatic)
    """
    ...

  def set_joint_acceleration(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the joint acceleration in state.qd.
    
    :param str name: joint name 
    
    :param float value: joint acceleration
    """
    ...

  def set_joint_limits(
    self,
    name: str, # const std::string &
    lower: float, # double
    upper: float, # double
  ) -> None:
    """
    Sets the limits for a given joint.
    
    :param str name: joint name 
    
    :param float lower: lower limit 
    
    :param float upper: upper limit
    """
    ...

  def set_joint_velocity(
    self,
    name: str, # const std::string &
    value: float, # double
  ) -> None:
    """
    Sets the joint velocity in state.qd.
    
    :param str name: joint name 
    
    :param float value: joint velocity
    """
    ...

  def set_rotor_inertia(
    self,
    joint_name: str, # const std::string &
    rotor_inertia: float, # double
  ) -> None:
    """
    Updates the rotor inertia (used for apparent inertia computation in the dynamics)
    """
    ...

  def set_torque_limit(
    self,
    name: str, # const std::string &
    limit: float, # double
  ) -> None:
    """
    Sets the torque limit for a given joint.
    
    :param str name: joint name 
    
    :param float limit: torque limit
    """
    ...

  def set_velocity_limit(
    self,
    name: str, # const std::string &
    limit: float, # double
  ) -> None:
    """
    Sets the velocity limit for a given joint.
    
    :param str name: joint name 
    
    :param float limit: joint limit
    """
    ...

  def set_velocity_limits(
    self,
    limit: float, # double
  ) -> None:
    """
    Set the velocity limits for all the joints.
    
    :param float limit: limit
    """
    ...

  state: RobotWrapper_State # placo::model::RobotWrapper::State
  """
  Robot's current state.
  """

  def static_gravity_compensation_torques(
    self,
    frameIndex: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Computes torques needed by the robot to compensate for the generalized gravity, assuming that the given frame is the (only) contact supporting the robot.
    """
    ...

  def static_gravity_compensation_torques_dict(
    arg1: RobotWrapper,
    arg2: str,
  ) -> dict:
    ...

  def torques_from_acceleration_with_fixed_frame(
    self,
    qdd_a: numpy.ndarray, # Eigen::VectorXd
    frameIndex: any, # pinocchio::FrameIndex
  ) -> numpy.ndarray:
    """
    Computes required torques in the robot DOFs for a given acceleration of the actuated DOFs, assuming that the given frame is fixed.
    
    :param numpy.ndarray qdd_a: acceleration of the actuated DOFs
    """
    ...

  def torques_from_acceleration_with_fixed_frame_dict(
    self: RobotWrapper,
    qdd_a: numpy.ndarray,
    frame: str,
  ) -> dict:
    """
    Computes the torque required to reach given acceleration in fixed frame
    """
    ...

  def total_mass(
    self,
  ) -> float:
    """
    Total mass.
    """
    ...

  def update_kinematics(
    self,
  ) -> None:
    """
    Update internal computation for kinematics (frames, jacobian). This method should be called when the robot state has changed.
    """
    ...

  visual_model: any # pinocchio::GeometryModel
  """
  Pinocchio visual model.
  """


class RobotWrapper_State:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  q: numpy.ndarray # Eigen::VectorXd
  """
  joints configuration $q$
  """

  qd: numpy.ndarray # Eigen::VectorXd
  """
  joints velocity $\dot q$
  """

  qdd: numpy.ndarray # Eigen::VectorXd
  """
  joints acceleration $\ddot q$
  """


class Segment:
  def Segment(
    self,
  ) -> any:
    ...

  end: numpy.ndarray # Eigen::Vector2d

  def half_line_pass_through(
    self,
    s: Segment, # placo::tools::Segment
  ) -> bool:
    """
    Checks if the half-line starting from the start of this segment and going through its end pass through another segment.
    
    :param Segment s: The other segment.
    """
    ...

  def intersects(
    self,
    s: Segment, # placo::tools::Segment
  ) -> bool:
    """
    Checks if there is an intersection between this segment and another one, i.e. if the intersection of their guiding lines is a point of both segments.
    
    :param Segment s: The other segment.
    """
    ...

  def is_collinear(
    self,
    s: Segment, # placo::tools::Segment
    epsilon: float = 1e-6, # double
  ) -> bool:
    """
    Checks if this segment is collinear with another one.
    
    :param Segment s: The segment to check collinearity with. 
    
    :param float epsilon: To account for floating point errors.
    """
    ...

  def is_parallel(
    self,
    s: Segment, # placo::tools::Segment
    epsilon: float = 1e-6, # double
  ) -> bool:
    """
    Checks if this segment is parallel to another one.
    
    :param Segment s: The segment to check parallelism with. 
    
    :param float epsilon: To account for floating point errors.
    """
    ...

  def is_point_aligned(
    self,
    point: numpy.ndarray, # const Eigen::Vector2d &
    epsilon: float = 1e-6, # double
  ) -> bool:
    """
    Checks if a point is aligned with this segment.
    
    :param numpy.ndarray point: The point to check alignment with. 
    
    :param float epsilon: To account for floating point errors.
    """
    ...

  def is_point_in_segment(
    self,
    point: numpy.ndarray, # const Eigen::Vector2d &
    epsilon: float = 1e-6, # double
  ) -> bool:
    """
    Checks if a point is in the segment.
    
    :param numpy.ndarray point: The point to check. 
    
    :param float epsilon: To account for floating point errors.
    """
    ...

  def line_pass_through(
    self,
    s: Segment, # placo::tools::Segment
  ) -> bool:
    """
    Checks if the guiding line of another segment pass through this segment, i.e. if the intersection between the guiding lines of this segment and another one is a point of this segment.
    
    :param Segment s: The other segment.
    """
    ...

  def lines_intersection(
    self,
    s: Segment, # placo::tools::Segment
  ) -> numpy.ndarray:
    """
    Return the intersection between the guiding lines of this segment and another one.
    
    :param Segment s: The other segment.
    """
    ...

  start: numpy.ndarray # Eigen::Vector2d


class Sparsity:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def add_interval(
    self,
    start: int, # int
    end: int, # int
  ) -> None:
    """
    Adds an interval to the sparsity, this will compute the union of intervals.
    
    :param int start: interval start 
    
    :param int end: interval end
    """
    ...

  @staticmethod
  def detect_columns_sparsity(
    self,
    M: numpy.ndarray, # const Eigen::MatrixXd
  ) -> Sparsity:
    """
    Helper to detect columns sparsity.
    
    :param numpy.ndarray M: given matrix
    """
    ...

  intervals: list[SparsityInterval] # std::vector<placo::problem::Sparsity::Interval>
  """
  Intervals of non-sparse columns.
  """

  def print_intervals(
    self,
  ) -> None:
    """
    Print intervals.
    """
    ...


class SparsityInterval:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  end: int # int
  """
  End of interval.
  """

  start: int # int
  """
  Start of interval.
  """


class Support:
  def Support(
    self,
  ) -> any:
    ...

  def apply_offset(
    self,
    offset: numpy.ndarray, # Eigen::Vector2d
  ) -> None:
    ...

  elapsed_ratio: float # double

  end: bool # bool

  def footstep_frame(
    self,
    side: any, # placo::humanoid::HumanoidRobot::Side
  ) -> numpy.ndarray:
    """
    Returns the frame for a given side (if present)
    
    :param any side: the side we want the frame (left or right foot)
    """
    ...

  footsteps: list[Footstep] # std::vector<placo::humanoid::FootstepsPlanner::Footstep>

  def frame(
    self,
  ) -> numpy.ndarray:
    """
    Returns the frame for the support. It will be the (interpolated) average of footsteps frames.
    """
    ...

  def is_both(
    self,
  ) -> bool:
    """
    Checks whether this support is a double support.
    """
    ...

  replanned: bool # bool

  def set_end(
    arg1: Support,
    arg2: bool,
  ) -> None:
    ...

  def set_start(
    arg1: Support,
    arg2: bool,
  ) -> None:
    ...

  def side(
    self,
  ) -> any:
    """
    The support side (you should call is_both() to be sure it's not a double support before)
    """
    ...

  start: bool # bool

  def support_polygon(
    self,
  ) -> list[numpy.ndarray]:
    ...

  t_start: float # double

  time_ratio: float # double


class Supports:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def append(
    arg1: Supports,
    arg2: object,
  ) -> None:
    ...

  def extend(
    arg1: Supports,
    arg2: object,
  ) -> None:
    ...


class SwingFoot:
  """
  A cubic fitting of swing foot, see: https://scaron.info/doc/pymanoid/walking-pattern-generation.html#pymanoid.swing_foot.SwingFoot.
  """
  def __init__(
    arg1: object,
  ) -> None:
    ...

  @staticmethod
  def make_trajectory(
    self,
    t_start: float, # double
    t_end: float, # double
    height: float, # double
    start: numpy.ndarray, # Eigen::Vector3d
    target: numpy.ndarray, # Eigen::Vector3d
  ) -> SwingFootTrajectory:
    ...

  @staticmethod
  def remake_trajectory(
    self,
    old_trajectory: SwingFootTrajectory, # placo::humanoid::SwingFoot::Trajectory
    t: float, # double
    target: numpy.ndarray, # Eigen::Vector3d
  ) -> SwingFootTrajectory:
    ...


class SwingFootCubic:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  @staticmethod
  def make_trajectory(
    self,
    t_start: float, # double
    virt_duration: float, # double
    height: float, # double
    rise_ratio: float, # double
    start: numpy.ndarray, # Eigen::Vector3d
    target: numpy.ndarray, # Eigen::Vector3d
    elapsed_ratio: float = 0., # double
    start_vel: numpy.ndarray = None, # Eigen::Vector3d (default: Eigen::Vector3d::Zero())
  ) -> SwingFootCubicTrajectory:
    ...


class SwingFootCubicTrajectory:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def pos(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def vel(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...


class SwingFootQuintic:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  @staticmethod
  def make_trajectory(
    self,
    t_start: float, # double
    t_end: float, # double
    height: float, # double
    start: numpy.ndarray, # Eigen::Vector3d
    target: numpy.ndarray, # Eigen::Vector3d
  ) -> SwingFootQuinticTrajectory:
    ...


class SwingFootQuinticTrajectory:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def pos(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def vel(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...


class SwingFootTrajectory:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def pos(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def vel(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...


class Task:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  def __init__(
  ) -> any:
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  name: str # std::string
  """
  Object name.
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class TaskContact:
  def TaskContact(
    self,
    task: DynamicsTask, # placo::dynamics::Task
  ) -> any:
    """
    see DynamicsSolver::add_task_contact
    """
    ...

  active: bool # bool
  """
  true if the contact is active (ignored by the solver else, this allow to enable/disable a contact without removing it from the solver)
  """

  mu: float # double
  """
  Coefficient of friction (if relevant)
  """

  weight_forces: float # double
  """
  Weight of forces for the optimization (if relevant)
  """

  weight_moments: float # double
  """
  Weight of moments for optimization (if relevant)
  """

  weight_tangentials: float # double
  """
  Extra cost for tangential forces.
  """

  wrench: numpy.ndarray # Eigen::VectorXd
  """
  Wrench populated after the DynamicsSolver::solve call.
  """


class Variable:
  """
  Represents a variable in a Problem.
  """
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def expr(
    self,
    start: int = -1, # int
    rows: int = -1, # int
  ) -> Expression:
    """
    Builds an expression from a variable.
    
    :param int start: start row (default: 0) 
    
    :param int rows: number of rows (default: -1, all rows)
    """
    ...

  k_end: int # int
  """
  End offset in the Problem.
  """

  k_start: int # int
  """
  Start offset in the Problem.
  """

  value: numpy.ndarray # Eigen::VectorXd
  """
  Variable value, populated by Problem after a solve.
  """


class WPGTrajectory:
  def __init__(
    arg1: object,
    arg2: float,
    arg3: float,
    arg4: float,
  ) -> None:
    ...

  def apply_transform(
    self,
    T: numpy.ndarray, # Eigen::Affine3d
  ) -> None:
    """
    Applies a given transformation to the left of all values issued by the trajectory.
    """
    ...

  com_target_z: float # double

  def get_R_world_trunk(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_T_world_left(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_T_world_right(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_a_world_CoM(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_j_world_CoM(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_next_support(
    self,
    t: float, # double
    n: int = 1, # int
  ) -> Support:
    """
    Returns the nth next support corresponding to the given time in the trajectory.
    """
    ...

  def get_p_world_CoM(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_p_world_DCM(
    self,
    t: float, # double
    omega: float, # double
  ) -> numpy.ndarray:
    ...

  def get_p_world_ZMP(
    self,
    t: float, # double
    omega: float, # double
  ) -> numpy.ndarray:
    ...

  def get_part_end_dcm(
    self,
    t: float, # double
    omega: float, # double
  ) -> numpy.ndarray:
    """
    Returns the DCM at the end of the trajectory part corresponding to the given time.
    """
    ...

  def get_part_t_end(
    self,
    t: float, # double
  ) -> float:
    """
    Returns the end time of the trajectory part corresponding to the given time.
    """
    ...

  def get_part_t_start(
    self,
    t: float, # double
  ) -> float:
    """
    Returns the start time of the trajectory part corresponding to the given time.
    """
    ...

  def get_prev_support(
    self,
    t: float, # double
    n: int = 1, # int
  ) -> Support:
    """
    Returns the nth previous support corresponding to the given time in the trajectory.
    """
    ...

  def get_support(
    self,
    t: float, # double
  ) -> Support:
    """
    Returns the support corresponding to the given time in the trajectory.
    """
    ...

  def get_supports(
    self,
  ) -> list[Support]:
    ...

  def get_v_world_CoM(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_v_world_foot(
    self,
    side: any, # placo::humanoid::HumanoidRobot::Side
    t: float, # double
  ) -> numpy.ndarray:
    ...

  def get_v_world_right(
    self,
    t: float, # double
  ) -> numpy.ndarray:
    ...

  kept_ts: int # int

  def print_parts_timings(
    self,
  ) -> None:
    ...

  def support_is_both(
    self,
    t: float, # double
  ) -> bool:
    ...

  def support_side(
    self,
    t: float, # double
  ) -> any:
    ...

  t_end: float # double

  t_start: float # double

  trunk_pitch: float # double

  trunk_roll: float # double


class WPGTrajectoryPart:
  def __init__(
    arg1: object,
    arg2: Support,
    arg3: float,
  ) -> None:
    ...

  support: Support # placo::humanoid::FootstepsPlanner::Support

  t_end: float # double

  t_start: float # double


class WalkPatternGenerator:
  def WalkPatternGenerator(
    self,
    robot: HumanoidRobot, # placo::humanoid::HumanoidRobot
    parameters: HumanoidParameters, # placo::humanoid::HumanoidParameters
  ) -> any:
    ...

  def can_replan_supports(
    self,
    trajectory: WPGTrajectory, # placo::humanoid::WalkPatternGenerator::Trajectory
    t_replan: float, # double
  ) -> bool:
    """
    Checks if a trajectory can be replanned for supports.
    """
    ...

  def get_optimal_zmp(
    self,
    world_dcm_start: numpy.ndarray, # Eigen::Vector2d
    world_dcm_end: numpy.ndarray, # Eigen::Vector2d
    duration: float, # double
    support: Support, # placo::humanoid::FootstepsPlanner::Support
  ) -> numpy.ndarray:
    """
    Computes the best ZMP in the support polygon to move de DCM from world_dcm_start to world_dcm_end in duration.
    
    :param numpy.ndarray world_dcm_start: The initial DCM position in world frame 
    
    :param numpy.ndarray world_dcm_end: The desired final DCM position in world frame 
    
    :param float duration: The duration 
    
    :param Support support: The support
    """
    ...

  def plan(
    self,
    supports: list[Support], # std::vector<placo::humanoid::FootstepsPlanner::Support>
    initial_com_world: numpy.ndarray, # Eigen::Vector3d
    t_start: float = 0., # double
  ) -> WPGTrajectory:
    """
    Plans a walk trajectory following given footsteps based on the parameters of the WPG.
    
    :param list[Support] supports: Supports generated from the foosteps to follow
    """
    ...

  def replan(
    self,
    supports: list[Support], # std::vector<placo::humanoid::FootstepsPlanner::Support>
    old_trajectory: WPGTrajectory, # placo::humanoid::WalkPatternGenerator::Trajectory
    t_replan: float, # double
  ) -> WPGTrajectory:
    """
    Updates the walk trajectory to follow given footsteps based on the parameters of the WPG.
    
    :param list[Support] supports: Supports generated from the current foosteps or the new ones to follow. Contain the current support 
    
    :param WPGTrajectory old_trajectory: Current walk trajectory 
    
    :param float t_replan: The time (in the original trajectory) where the replan happens
    """
    ...

  def replan_supports(
    self,
    planner: FootstepsPlanner, # placo::humanoid::FootstepsPlanner
    trajectory: WPGTrajectory, # placo::humanoid::WalkPatternGenerator::Trajectory
    t_replan: float, # double
    t_last_replan: float, # double
  ) -> list[Support]:
    """
    Replans the supports for a given trajectory given a footsteps planner.
    """
    ...

  def update_supports(
    self,
    t: float, # double
    supports: list[Support], # std::vector<placo::humanoid::FootstepsPlanner::Support>
    world_measured_dcm: numpy.ndarray, # Eigen::Vector2d
    world_end_dcm: numpy.ndarray, # Eigen::Vector2d
  ) -> list[Support]:
    """
    Updates the supports to ensure DCM viability by adjusting the duration and the target of the current swing trajectory.
    
    :param float t: The current time 
    
    :param list[Support] supports: The planned supports 
    
    :param numpy.ndarray world_measured_dcm: The measured DCM in world frame 
    
    :param numpy.ndarray world_end_dcm: The desired DCM at the end of the current support phase
    """
    ...


class WalkTasks:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  com_x: float # double

  com_y: float # double

  def get_tasks_error(
    self,
  ) -> dict[str, numpy.ndarray]:
    ...

  def initialize_tasks(
    self,
    solver: KinematicsSolver, # placo::kinematics::KinematicsSolver
    robot: HumanoidRobot, # placo::humanoid::HumanoidRobot
  ) -> None:
    ...

  left_foot_task: FrameTask # placo::kinematics::FrameTask

  def reach_initial_pose(
    self,
    T_world_left: numpy.ndarray, # Eigen::Affine3d
    feet_spacing: float, # double
    com_height: float, # double
    trunk_pitch: float, # double
  ) -> None:
    ...

  def remove_tasks(
    self,
  ) -> None:
    ...

  right_foot_task: FrameTask # placo::kinematics::FrameTask

  scaled: bool # bool

  solver: KinematicsSolver # placo::kinematics::KinematicsSolver

  trunk_mode: bool # bool

  trunk_orientation_task: OrientationTask # placo::kinematics::OrientationTask

  def update_tasks(
    self,
    trajectory: WPGTrajectory, # placo::humanoid::WalkPatternGenerator::Trajectory
    t: float, # double
  ) -> None:
    ...

  def update_tasks_from_trajectory(
    arg1: WalkTasks,
    arg2: WPGTrajectory,
    arg3: float,
  ) -> None:
    ...


class WheelTask:
  A: numpy.ndarray # Eigen::MatrixXd
  """
  Matrix A in the task Ax = b, where x are the joint delta positions.
  """

  T_world_surface: numpy.ndarray # Eigen::Affine3d
  """
  Target position in the world.
  """

  def WheelTask(
    self,
    joint: str, # std::string
    radius: float, # double
    omniwheel: bool = False, # bool
  ) -> any:
    """
    See KinematicsSolver::add_wheel_task.
    """
    ...

  b: numpy.ndarray # Eigen::MatrixXd
  """
  Vector b in the task Ax = b, where x are the joint delta positions.
  """

  def configure(
    self,
    name: str, # std::string
    priority: str = "soft", # std::string
    weight: float = 1.0, # double
  ) -> None:
    """
    Configures the object.
    
    :param str name: task name 
    
    :param str priority: task priority (hard, soft or scaled) 
    
    :param float weight: task weight
    """
    ...

  def error(
    self,
  ) -> numpy.ndarray:
    """
    Task errors (vector)
    """
    ...

  def error_norm(
    self,
  ) -> float:
    """
    The task error norm.
    """
    ...

  joint: str # std::string
  """
  Frame.
  """

  name: str # std::string
  """
  Object name.
  """

  omniwheel: bool # bool
  """
  Omniwheel (can slide laterally)
  """

  priority: any # placo::kinematics::ConeConstraint::Priority
  """
  Object priority.
  """

  radius: float # double
  """
  Wheel radius.
  """

  def update(
    self,
  ) -> None:
    """
    Update the task A and b matrices from the robot state and targets.
    """
    ...


class boost_type_index:
  def __init__(
  ) -> any:
    ...

  def hash_code(
    self: boost_type_index,
  ) -> int:
    """
    Returns an unspecified value (here denoted by hash code) such that for all std::type_info objects referring to the same type, their hash code is the same.
    """
    ...

  def name(
    self: boost_type_index,
  ) -> str:
    """
    Returns an implementation defined null-terminated character string containing the name of the type. No guarantees are given; in particular, the returned string can be identical for several types and change between invocations of the same program.
    """
    ...

  def pretty_name(
    self: boost_type_index,
  ) -> str:
    """
    Human readible name.
    """
    ...


def directions_2d(
  n: int, # int
) -> numpy.ndarray:
  """
  Generates a set of directions in 2D.
  
  :param int n: the number of directions
  """
  ...


def directions_3d(
  n: int, # int
  epsilon: float = 0.5, # double
) -> numpy.ndarray:
  """
  Generates a set of directions in 3D, using Fibonacci lattice.
  
  :param int n: the number of directions 
  
  :param float epsilon: the epsilon parameter for the Fibonacci lattice
  """
  ...


def flatten_on_floor(
  transformation: numpy.ndarray, # const Eigen::Affine3d &
) -> numpy.ndarray:
  """
  Takes a 3D transformation and ensure it is "flat" on the floor (setting z to 0 and keeping only yaw)
  
  :param numpy.ndarray transformation: a 3D transformation
  """
  ...


def frame_yaw(
  rotation: numpy.ndarray, # Eigen::Matrix3d
) -> float:
  """
  Computes the "yaw" of an orientation.
  
  :param numpy.ndarray rotation: the orientation
  """
  ...


def interpolate_frames(
  frameA: numpy.ndarray, # Eigen::Affine3d
  frameB: numpy.ndarray, # Eigen::Affine3d
  AtoB: float, # double
) -> numpy.ndarray:
  """
  Interpolate between two frames.
  
  :param numpy.ndarray frameA: Frame A 
  
  :param numpy.ndarray frameB: Frame B 
  
  :param float AtoB: A real number from 0 to 1 that controls the interpolation (0: frame A, 1: frameB)
  """
  ...


class map_indexing_suite_map_string_double_entry:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def data(
    arg1: map_indexing_suite_map_string_double_entry,
  ) -> float:
    ...

  def key(
    arg1: map_indexing_suite_map_string_double_entry,
  ) -> str:
    ...


class map_string_double:
  def __init__(
    arg1: object,
  ) -> None:
    ...


def optimal_transformation(
  points_in_A: numpy.ndarray, # Eigen::MatrixXd
  points_in_B: numpy.ndarray, # Eigen::MatrixXd
) -> numpy.ndarray:
  """
  Finds the optimal transformation T_a_b that minimizes the sum of squared distances between the (same) points with coordinates expressed in A and B. Points are stacked in lines (columns are x, y and z) in the matrices.
  """
  ...


def rotation_from_axis(
  axis: str, # std::string
  vector: numpy.ndarray, # Eigen::Vector3d
) -> numpy.ndarray:
  """
  Builds a rotation matrix with a given axis target.
  
  :param str axis: axis (x, y or z) 
  
  :param numpy.ndarray vector: target (unit) vector
  """
  ...


def seed(
  seed_value: int,
) -> None:
  """
  Initialize the pseudo-random number generator with the argument seed_value.
  """
  ...


def sharedMemory(
  value: bool,
) -> None:
  """
  Share the memory when converting from Eigen to Numpy.
  """
  ...


class std_type_index:
  def __init__(
  ) -> any:
    ...

  def hash_code(
    self: std_type_index,
  ) -> int:
    """
    Returns an unspecified value (here denoted by hash code) such that for all std::type_info objects referring to the same type, their hash code is the same.
    """
    ...

  def name(
    self: std_type_index,
  ) -> str:
    """
    Returns an implementation defined null-terminated character string containing the name of the type. No guarantees are given; in particular, the returned string can be identical for several types and change between invocations of the same program.
    """
    ...

  def pretty_name(
    self: std_type_index,
  ) -> str:
    """
    Human readible name.
    """
    ...


class vector_Collision:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def append(
    arg1: vector_Collision,
    arg2: object,
  ) -> None:
    ...

  def extend(
    arg1: vector_Collision,
    arg2: object,
  ) -> None:
    ...


class vector_Distance:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def append(
    arg1: vector_Distance,
    arg2: object,
  ) -> None:
    ...

  def extend(
    arg1: vector_Distance,
    arg2: object,
  ) -> None:
    ...


class vector_MatrixXd:
  def __init__(
    arg1: object,
  ) -> None:
    ...

  def append(
    arg1: vector_MatrixXd,
    arg2: object,
  ) -> None:
    ...

  def extend(
    arg1: vector_MatrixXd,
    arg2: object,
  ) -> None:
    ...


def wrap_angle(
  angle: float, # double
) -> float:
  """
  Wraps an angle between -pi and pi.
  """
  ...


__groups__ = {'placo::dynamics': ['AvoidSelfCollisionsDynamicsConstraint', 'Contact', 'Contact6D', 'DynamicsCoMTask', 'DynamicsConstraint', 'DynamicsFrameTask', 'DynamicsGearTask', 'DynamicsJointsTask', 'DynamicsOrientationTask', 'DynamicsPositionTask', 'DynamicsRelativeFrameTask', 'DynamicsRelativeOrientationTask', 'DynamicsRelativePositionTask', 'DynamicsSolver', 'DynamicsSolverResult', 'DynamicsTask', 'DynamicsTorqueTask', 'ExternalWrenchContact', 'LineContact', 'PointContact', 'PuppetContact', 'TaskContact'], 'placo::kinematics': ['AvoidSelfCollisionsKinematicsConstraint', 'AxisAlignTask', 'CentroidalMomentumTask', 'CoMPolygonConstraint', 'CoMTask', 'ConeConstraint', 'DistanceTask', 'FrameTask', 'GearTask', 'JointSpaceHalfSpacesConstraint', 'JointsTask', 'KinematicsConstraint', 'KinematicsSolver', 'KineticEnergyRegularizationTask', 'ManipulabilityTask', 'OrientationTask', 'PositionTask', 'RegularizationTask', 'RelativeFrameTask', 'RelativeOrientationTask', 'RelativePositionTask', 'Task', 'WheelTask'], 'placo::tools': ['AxisesMask', 'CubicSpline', 'CubicSpline3D', 'Polynom', 'Prioritized', 'Segment'], 'placo::model': ['Collision', 'Distance', 'RobotWrapper', 'RobotWrapper_State'], 'placo::problem': ['Expression', 'Integrator', 'IntegratorTrajectory', 'PolygonConstraint', 'Problem', 'ProblemConstraint', 'ProblemPolynom', 'QPError', 'Sparsity', 'SparsityInterval', 'Variable'], 'placo::humanoid': ['Footstep', 'FootstepsPlanner', 'FootstepsPlannerNaive', 'FootstepsPlannerRepetitive', 'HumanoidParameters', 'HumanoidRobot', 'LIPM', 'LIPMTrajectory', 'Support', 'SwingFoot', 'SwingFootCubic', 'SwingFootCubicTrajectory', 'SwingFootQuintic', 'SwingFootQuinticTrajectory', 'SwingFootTrajectory', 'WPGTrajectory', 'WPGTrajectoryPart', 'WalkPatternGenerator', 'WalkTasks']}
