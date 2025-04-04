'''
Original COMPleib MATLAB function
(partially) converted to a Python function
Web: http://www.friedemann-leibfritz.de/COMPlib_Data/Matlab_COMPlib_r1_1.zip
'''
from typing import Tuple, Optional, Union, List, Callable

import numpy as np

SUPPORTED_COMPLEIB_SYSTEMS = {
    # ACx - Aircraft models
    'AC1', 'AC2', 'AC3', 'AC4', 'AC5', 'AC6', 'AC7',
    'AC8', 'AC11', 'AC12', 'AC15', 'AC16', 'AC17',

    # HEx - Helicopter models
    'HE1', 'HE2', 'HE3', 'HE4', 'HE5',

    # REAx - Reactor models
    'REA1', 'REA2', 'REA3', 'REA4',

    # DISx - Decentralized interconnected systems
    'DIS1', 'DIS2', 'DIS3', 'DIS4', 'DIS5',

    # TG1 - a 1072 MVA nuclear-powered turbo-generator
    'TG1',

    # AGS - an automobile gas turbine
    'AGS',

    # BDT1 - a fairly realistic model of a binary distillation tower
    'BDT1',

    # MFP - a moored floating platform
    'MFP',

    # UWV - a control surface servo for an underwater vehicle
    'UWV',

    # EBx - Euler-Bernoulli beam
    'EB1', 'EB2',

    # PAS - a piezoelectric bimorph actuator system design
    'PAS',

    # TF - a terrain following model
    'TF1', 'TF2', 'TF3',

    # PSM - a two-area interconnected power system
    'PSM',

    # NNx - Academic test problems
    'NN1', 'NN2', 'NN3', 'NN4', 'NN5', 'NN6', 'NN7',
    'NN8', 'NN9', 'NN10', 'NN11', 'NN12',
    'NN13', 'NN14', 'NN15', 'NN16', 'NN17',

    # DLRx - models of a space structure
    'DLR1',

    # ROCx - reduced order control problems
    'ROC1', 'ROC2', 'ROC3', 'ROC4',
    'ROC5', 'ROC6', 'ROC7', 'ROC8', 'ROC9', 'ROC10',
}


def get_model_from_compleib(env_id: str) -> Optional[Tuple]:
    if env_id not in SUPPORTED_COMPLEIB_SYSTEMS:
        return None

    try:
        A, B1, B, *_ = COMPleib(env_id)
        return True, A, B, B1
    except Exception as e:
        return None


def strmatch(env_id: str, input_id: str, mode: str) -> bool:
    return env_id == input_id


def COMPleib(ex: str) -> Tuple:
    #  COMPleib: COnstrained Matrix-optimization Problem library

    #   Version: 1.1
    #      Date: 09.03.2005 (last change)
    #    Author: Friedemann Leibfritz

    #     References:
    #     [1] COMPl{_e}ib: COnstrained Matrix-optimization Problem library --
    #         a collection of test examples for nonlinear semidefinite
    #         programs, control system design and related problems
    #         F. Leibfritz, Tech.-Report, 2003

    #     [2] COMPl{_e}ib 1.0 -- User manual and quick reference
    #         F. Leibfritz and W. Lipinski, Tech.-Report, 2004

    #     [3] Description of the benchmark examples in COMPl{_e}ib 1.0
    #         F. Leibfritz and W. Lipinski, Tech.-Report, 2003

    #  Input: ex -- string variable which refers to an example in COMPlib,
    #                i.e. 'AC1'. For more details, i.e., see [2], [3]

    #  Output: data matrices
    #            A -- real (nx times nx) matrix
    #            B -- real (nx times nu) matrix
    #            C -- real (ny times nx) matrix
    #           B1 -- real (nx times nw) matrix
    #           C1 -- real (nz times nx) matrix
    #          D11 -- real (nz times nw) matrix
    #          D12 -- real (nz times nu) matrix
    #          D21 -- real (ny times nw) matrix
    #           nx -- dimension of the 'state'
    #           nu -- dimension of the 'control'
    #           ny -- dimension of the 'measurement'
    #           nw -- dimension of the 'noise'
    #           nz -- dimension of the 'regulated output'

    #  Note: From the output data of COMPleib, one can define a control
    #        system of the form

    #        (d/dt)x(t) =  A*x(t)+ B1*w(t)+ B*u(t);  (x - state, u - control, w- noise)
    #              z(t) = C1*x(t)+D11*w(t)+D12*u(t); (z - reg. output)
    #              y(t) =  C*x(t)+D21*w(t).          (y - measurement)

    #        Depending on the control design goals, from the COMPleib data
    #        it is possible to form several constraint matrix optimization
    #        problems, i.e.
    #          --- nonlinear semidefinite programs (NSDPs)
    #          --- or, equivalently, bilinear matrix inequality (BMI) problems
    #          --- linear semidefinite programs.
    #        For more details, see [1], [2].

    ##########################################################################
    A = []
    B1 = []
    B = []
    C1 = []
    C = []
    D11 = []
    D12 = []
    D21 = []
    ny = None
    nw = None
    nz = None

    # ------------------------------------------------------------------
    # (AC1)/(AC2): Y. S. Hung and A. G. J. MacFarlane, "Multivariable
    #              feedback: A quasi--classical approach", Springer-Verlag,
    #              "Lecture Notes in Control and Information Sciences",
    #              1982
    # ------------------------------------------------------------------
    if strmatch('AC1', ex, 'exact'):
        nx = 5
        nu = 3
        ny = 3
        A = np.array([[0, 0, 1.132, 0, - 1], [0, - 0.0538, - 0.1712, 0, 0.0705], [0, 0, 0, 1, 0],
                      [0, 0.0485, 0, - 0.8556, - 1.013], [0, - 0.2909, 0, 1.0532, - 0.6859]])
        B = np.array([[0, 0, 0], [- 0.12, 1, 0], [0, 0, 0], [4.419, 0, - 1.665], [1.575, 0, - 0.0732]])
        C = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
        B1 = np.array(
            [[0.03593, 0, 0.01672], [0, 0.00989, 0], [0, - 0.07548, 0], [0, 0, 0.05635], [0.00145, 0, 0.06743]])

        D12 = (1 / np.sqrt(2)) * np.array([[1, 0, 0], [0, 1, 0]])
        nx, nw = B1.shape
        # nz, nx = C1.shape
        nz, nu = D12.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))



    # ------------------------------------------------------------------
    # (AC2): like (AC1) with changed C1, D11, D12
    # ------------------------------------------------------------------
    elif strmatch('AC2', ex, 'exact'):
        nx = 5
        nu = 3
        ny = 3
        A = np.array([[0, 0, 1.132, 0, - 1], [0, - 0.0538, - 0.1712, 0, 0.0705], [0, 0, 0, 1, 0],
                      [0, 0.0485, 0, - 0.8556, - 1.013], [0, - 0.2909, 0, 1.0532, - 0.6859]])
        B = np.array([[0, 0, 0], [- 0.12, 1, 0], [0, 0, 0], [4.419, 0, - 1.665], [1.575, 0, - 0.0732]])
        C = np.array([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
        B1 = np.array(
            [[0.03593, 0, 0.01672], [0, 0.00989, 0], [0, - 0.07548, 0], [0, 0, 0.05635], [0.00145, 0, 0.06743]])
        C1 = (1 / np.sqrt(2)) * np.array(
            [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        D12 = (1 / np.sqrt(2)) * np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
        nx, nw = B1.shape
        nz, nx = C1.shape
        nz, nu = D12.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))



    # ------------------------------------------------------------------
    # (AC3): L-1011 aircraft in cruise flight conditions
    #       C. Edwards and S. K. Spurgeon,
    #       On the development of discontinuous observers",
    #       IJOC, Vol. 59, Nr. 5, pp. 1211-1229, 1994
    # ------------------------------------------------------------------
    elif strmatch('AC3', ex, 'exact'):
        nx = 5
        nu = 2
        ny = 4
        A = np.array([[0, 0, 1, 0, 0], [0, - 0.154, - 0.0042, 1.54, 0], [0, 0.249, - 1, - 5.2, 0],
                      [0.0386, - 0.996, - 0.0003, - 0.117, 0], [0, 0.5, 0, 0, - 0.5]])
        B = np.array([[0, 0], [- 0.744, - 0.032], [0.337, - 1.12], [0.02, 0], [0, 0]])
        C = np.array([[0, 1, 0, 0, - 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0]])



    # ------------------------------------------------------------------
    # (AC4): Missile autopilot;  ##ehemals (MA1)
    #        B. Fares, P. Apkarian and D. Noll,
    #        "An Augmented Lagrangian Method for a Class of LMI-Constrained
    #        Problems in Robust Control Theory",
    #        IJOC, Vol. 74, Nr. 4, pp. 348-360
    # ------------------------------------------------------------------
    elif strmatch('AC4', ex, 'exact'):
        A = np.array([[- 0.876, 1, - 0.1209, 0], [8.9117, 0, - 130.75, 0], [0, 0, - 150, 0], [- 1, 0, 0, - 0.05]])
        B = np.array([[0], [0], [150], [0]])
        C = np.array([[- 1, 0, 0, 0], [0, - 1, 0, 0]])
        B1 = np.array([[0, 0], [0, 0], [0, 0], [0, 1]])
        C1 = np.array([[- 0.25, 0, 0, 3.487], [0, 0, - 3, 0]])
        D12 = np.array([[0], [3]])
        D11 = np.array([[0, 0.25], [0, 0]])
        D21 = np.array([[0, 1], [0.01, 0]])



    # ------------------------------------------------------------------
    # (AC5): Boeing B-747 aircraft
    #       T. Ishihara, H.-J. Guo and H. Takeda,
    #       "A Design of Discrete-Time Integral Controllers with
    #       Computation Delays via Loop Transfer Recovery",
    #       AUTO, Vol. 28, Nr. 3, pp. 599-603, 1992
    # ------------------------------------------------------------------
    elif strmatch('AC5', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 2
        A = np.array([[0.9801, 0.0003, - 0.098, 0.0038], [- 0.3868, 0.9071, 0.0471, - 0.0008],
                      [0.1591, - 0.0015, 0.9691, 0.0003], [- 0.0198, 0.0958, 0.0021, 1]])
        B = np.array([[- 0.0001, 0.0058], [0.0296, 0.0153], [0.0012, - 0.0908], [0.0015, 0.0008]])
        C = np.array([[1, 0, 0, 0], [0, 0, 0, 1]])



    # ------------------------------------------------------------------
    # (AC6): THE AIRCRAFT L- 1011 MODEL ???
    # ------------------------------------------------------------------
    elif strmatch('AC6', ex, 'exact'):
        nx = 7
        nu = 2
        ny = 4
        A = np.array([[0, 0, 1, 0, 0, 0, 0], [0, - 0.154, - 0.0042, 1.54, 0, - 0.744, - 0.032],
                      [0, 0.249, - 1, - 5.2, 0, 0.337, - 1.12], [0.0386, - 0.996, - 0.0003, - 2.117, 0, 0.02, 0],
                      [0, 0.5, 0, 0, - 4, 0, 0], [0, 0, 0, 0, 0, - 20, 0], [0, 0, 0, 0, 0, 0, - 25]])
        B = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [20, 0], [0, 25]])
        C = np.array([[0, - 0.154, - 0.0042, 1.54, 0, - 0.744, - 0.032], [0, 0.249, - 1, - 5.2, 0, 0.337, - 1.12],
                      [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]])



    # ------------------------------------------------------------------
    # (AC7): Transport Aircraft model (Boing flight condition VMIN)
    #        D. Gangsaas, K. R. Bruce, J. D. Blight and U.-L. Ly,
    #        "Application of Modern Synthesis to Aircraft Control:
    #        Three Case Studies", TOAC, Vol.31, Nr.11, pp.995-1014, 1986
    #        Case study III 2)
    # ------------------------------------------------------------------
    elif strmatch('AC7', ex, 'exact'):
        nx = 9
        nu = 1
        ny = 2
        A = np.array([[- 0.06254, 0.01888, 0, - 0.56141, - 0.02751, 0, 0.06254, - 0.00123, 0],
                      [0.01089, - 0.9928, 0.99795, 0.00097, - 0.07057, 0, - 0.01089, 0.06449, 0],
                      [0.07743, 1.6754, - 1.31111, - 0.0003, - 4.2503, 0, - 0.07743, - 0.10883, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, - 20.0, 20, 0, 0, 0], [0, 0, 0, 0, 0, - 30, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, - 0.88206, 0, 0], [0, 0, 0, 0, 0, 0, 0, - 0.88206, 0.00882],
                      [0, 0, 0, 0, 0, 0, 0, - 0.00882, - 0.88206]])
        B = np.array([[0], [0], [0], [0], [0], [30], [0], [0], [0]])
        C = np.array(
            [[- 0.00519, 0.47604, 0.00098, - 0.00031, 0.03378, 0, 0.00519, - 0.03086, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]])
        B1 = np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1.3282, 0, 0, 0],
             [0, 1.62671, 0, 0], [0, - 68.75283, 0, 0]])

        D12 = (1 / np.sqrt(2)) * np.array([1])
        D21 = np.array([[0, 0, 0, 0], [0, 0, 0, 1]])
        nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))



    # ------------------------------------------------------------------
    # (AC8): Transport Aircraft model (Boing flight condition CRUISE)
    #        (see (AC7)!)
    #        Case study II, p.1001/1012
    # ------------------------------------------------------------------
    elif strmatch('AC8', ex, 'exact'):
        nx = 9
        nu = 1
        ny = 5
        A = np.array([[- 0.01365, 0.178, 0.00017, - 0.561, - 0.03726, 0, 0.01365, - 0.01311, 0],
                      [- 0.01516, - 0.752, 1.001, 0.00127, - 0.06311, 0, 0.01516, 0.05536, 0],
                      [0.00107, 0.07896, - 0.8725, 0, - 3.399, 0, - 0.00107, - 0.00581, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, - 20.0, 10.72, 0, 0, 0], [0, 0, 0, 0, 0, - 50, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, - 0.4447, 0, 0], [0, 0, 0, 0, 0, 0, 0, - 0.4447, 0.0044],
                      [0, 0, 0, 0, 0, 0, 0, - 0.0044, - 0.4447]])
        B = np.array([[0], [0], [0], [0], [0], [50], [0], [0], [0]])
        C = np.array(
            [[0.00646, 0.3203, - 0.03358, 0, - 0.1032, 0, - 0.00646, - 0.02358, 0], [1, 0, 0, 0, 0, 0, - 1, 0, 0],
             [- 0.01365, 0.178, 0.00017, - 0.561, - 0.03726, 0, 0.01365, - 0.01311, 0],
             [0, - 13.58, 0, 13.58, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]])

        B1 = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 50, 0, 0, 0, 0, 0],
                       [0.9431, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1.155, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, - 48.82, 0, 0, 0, 0, 0, 0, 0, 0]])
        D12 = (1 / 2) * np.array([[1], [1]])
        D21 = np.array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
        nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))





    # ------------------------------------------------------------------
    # (AC11): CCV-type aircraft;
    #         A. T. Alexandridis and P. N. Paraskevopoulos, "A New Approach
    #         to Eigenstructure Assignment by Output Feedback",
    #         TOAC, Vol. 41, Nr. 7, pp. 1046-1050, 1996; Example 2
    # ------------------------------------------------------------------
    elif strmatch('AC11', ex, 'exact'):
        A = np.array([[- 1.341, 0.9933, 0, - 0.1689, - 0.2518], [43.223, - 0.8693, 0, - 17.251, - 1.5766],
                      [1.341, 0.0067, 0, 0.1689, 0.2518], [0, 0, 0, - 20, 0], [0, 0, 0, 0, - 20]])
        B = np.array([[0, 0], [0, 0], [0, 0], [20, 0], [0, 20]])
        C = np.array([[0, 0, 1, 0, 0], [47.76, - 0.268, 0, - 4.56, 4.45], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])



    # ------------------------------------------------------------------
    # (AC12): ASTOVL Aircraft    ##ehemals (AC9)
    #         S. Toffner-Clausen, "System Identification and Robust Control:
    #         A Case Study Approach", Springer-Verlag,
    #         "Advances in Industrial Conrol", 1996; p. 274
    # ------------------------------------------------------------------
    elif strmatch('AC12', ex, 'exact'):
        nx = 4
        nu = 3
        ny = 4
        A = np.array([[- 0.0017, 0.0413, - 5.3257, - 9.7565], [- 0.0721, - 0.3393, 49.5146, - 1.0097],
                      [- 0.0008, 0.0138, - 0.2032, 0.0009], [0, 0, 1, 0]])
        B = np.array([[0.2086, - 0.0005, - 0.0271], [- 0.0005, 0.2046, 0.0139], [- 0.0047, 0.0023, 0.1226], [0, 0, 0]])
        C = np.array(
            [[0, 0, 57.2958, 0], [0, 0, 0, 57.2958], [0.1045, - 0.9945, 0.1375, 51.5791], [- 0.0002, 0.0045, 0, 0]])
        B1 = np.array([[0.033, 0, 0], [0, 0.048, - 0.002], [- 0.064, 0, 0.34], [0, 0, 0.006]])
        C1 = (1 / np.sqrt(2)) * np.array([1, 0, 0, 0])
        D12 = (1 / np.sqrt(2)) * np.array([0, 0, 1])
        D21 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0.0212, 0, 0]])
        nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))



    # --------------------------------------------------------------------
    # (AC15) Mach 2.7 flight condition of a supersonic transport aircraft  ##ehemals(NN2)
    #        "Computation of Optimal Output Feedback Gains for Linear
    #        Multivariable Systems", TOAC, Vol. 19, pp. 257-258, 1974
    # --------------------------------------------------------------------
    elif strmatch('AC15', ex, 'exact'):
        A = np.array(
            [[- 0.037, 0.0123, 0.00055, - 1], [0, 0, 1, 0], [- 6.37, 0, - 0.23, 0.0618], [1.25, 0, 0.016, - 0.0457]])
        B = np.array([[0.00084, 0.000236], [0, 0], [0.08, 0.804], [- 0.0862, - 0.0665]])
        C = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        B1 = np.eye(A.shape[0])
        C1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        D12 = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 1]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))



    # --------------------------------------------------------------------
    # (AC16)  like (AC15) with changed C and D21  ##ehemals(NN3)
    # --------------------------------------------------------------------
    elif strmatch('AC16', ex, 'exact'):
        A = np.array(
            [[- 0.037, 0.0123, 0.00055, - 1], [0, 0, 1, 0], [- 6.37, 0, - 0.23, 0.0618], [1.25, 0, 0.016, - 0.0457]])
        B = np.array([[0.00084, 0.000236], [0, 0], [0.08, 0.804], [- 0.0862, - 0.0665]])
        C = np.eye(A.shape[0])
        B1 = np.eye(A.shape[0])
        C1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        D12 = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 1]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))



    # ------------------------------------------------------------------
    # (AC17): Leteral axis dynamic for a L-1011 aircraft
    #         A. R. Galimidi and B. R. Bramish
    #        "The constrained Lyapunov problem and its application
    #          to robust output feedback stabilization"
    #         TOAC Vol. 31,Nr. 5, pp.410-419, 1986
    # ------------------------------------------------------------------
    elif strmatch('AC17', ex, 'exact'):
        nx = 4
        nu = 1
        ny = 2
        A = np.array(
            [[- 2.98, 0.93, 0, - 0.034], [- 0.99, - 0.21, 0.035, - 0.0011], [0, 0, 0, 1], [0.39, - 5.555, 0, - 1.89]])
        B = np.array([[- 0.032], [0], [0], [- 1.6]])
        C = np.array([[0, 0, 1, 0], [0, 0, 0, 1]])



    # ------------------------------------------------------------------
    # (HE1): Longitudinal motion of a VTOL helicopter
    #        S. N. Singh and A. A. R. Coelho,
    #        "Nonlinear control of mismatched uncertain linear systems
    #        and application to control of aircraft",
    #        Journal of Dynamic Systems, Measurement and Control, Vol. 106,
    #        pp. 203-210, 1984
    # ------------------------------------------------------------------
    elif strmatch('HE1', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 1
        A = np.array(
            [[- 0.0366, 0.0271, 0.0188, - 0.4555], [0.0482, - 1.01, 0.0024, - 4.0208], [0.1002, 0.3681, - 0.707, 1.42],
             [0, 0, 1, 0]])
        B = np.array([[0.4422, 0.1761], [3.5446, - 7.5922], [- 5.52, 4.49], [0, 0]])
        C = np.array([0, 1, 0, 0]).reshape((1, -1))
        B1 = np.array([[0.04678, 0], [0.04572, 0.00988], [0.04369, 0.00111], [- 0.02179, 0]])
        C1 = (1 / np.sqrt(2)) * np.array([[2, 0, 0, 0], [0, 1, 0, 0]])
        D12 = (1 / np.sqrt(2)) * np.array([[1, 0], [0, 1]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # ------------------------------------------------------------------
    # (HE2): AH-64  HELICOPTER at 130 knots
    #        Ph. M. Fitzsimons, "Reducing the computation required to solve
    #        a standard minimax problem", AUTO, Vol.31, pp.1885-1887, 1995
    # ------------------------------------------------------------------
    elif strmatch('HE2', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 2
        A = np.array(
            [[- 0.0649, 0.0787, 0.1705, - 0.5616], [0.0386, - 0.939, 4.2277, 0.0198], [0.1121, - 0.4254, - 0.7968, 0],
             [0, 0, 1, 0]])
        B = np.array([[- 0.9454, 0.5313], [- 8.6476, - 10.769], [19.0824, - 2.8959], [0, 0]])
        C = np.array([[1, 0, 0, 0], [0, 0, 0, 1]])


    # ------------------------------------------------------------------
    # (HE3): Bell 201A-1 helicopter
    #        D.-W. Gu, P. Hr. Petkov and M. M. Konstantinov,
    #        "H_inf and H_2 Optimization Toolbox in SLICOT",
    #        SLICOT Working Note 1999-12,
    #        available via ftp: wgs.esat.kuleuven.ac.be/
    #                           pub/WGS/REPORTS/SLWN1999-12.ps.Z
    # ------------------------------------------------------------------
    elif strmatch('HE3', ex, 'exact'):
        nx = 8
        nu = 4
        ny = 6
        A = np.array([[- 0.0046, 0.038, 0.3259, - 0.0045, - 0.402, - 0.073, - 9.81, 0],
                      [- 0.1978, - 0.5667, 0.357, - 0.0378, - 0.2149, 0.5683, 0, 0],
                      [0.0039, - 0.0029, - 0.2947, 0.007, 0.2266, 0.0148, 0, 0],
                      [0.0133, - 0.0014, - 0.4076, - 0.0654, - 0.4093, 0.2674, 0, 9.81],
                      [0.0127, - 0.01, - 0.8152, - 0.0397, - 0.821, 0.1442, 0, 0],
                      [- 0.0285, - 0.0232, 0.1064, 0.0709, - 0.2786, - 0.7396, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0]])
        B = np.array([[0.0676, 0.1221, - 0.0001, - 0.0016], [- 1.1151, 0.1055, 0.0039, 0.0035],
                      [0.0062, - 0.0682, 0.001, - 0.0035], [- 0.017, 0.0049, 0.1067, 0.1692],
                      [- 0.0129, 0.0106, 0.2227, 0.143], [0.139, 0.0059, 0.0326, - 0.407], [0, 0, 0, 0], [0, 0, 0, 0]])
        C = np.array(
            [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]])
        # C1 = np.array([[C], [np.zeros((4, 8))]])
        C1 = None
        # D12 = np.array([[np.zeros((6, 4))], [np.eye(4)]])
        # B1 = B[:, 1]
        D21 = 0.1 * np.array([[0], [1], [0], [0], [0.5], [0]])
        # nx, nw = B1.shape
        # nz, nx = C1.shape
        nz, nx = None, None
        # D11 = np.zeros((nz, nw))


    # ------------------------------------------------------------------
    # (HE4): Helicopter control
    #        "Multivariable feedback control: Analysis and design"
    #        S. Skogestad and I. Postlethwaite
    #        John Wiley and Sons, 1996, Section 12.2
    #        Note: Matlab files
    #              http://www.nt.ntnu.no/users/skoge/book/matlab.html
    #        stored in  /export/home/leibfr/Lipinski/matlab/..
    #                                ..Examples_Multi_Feedback_Control/matlab_m/
    #        F. Leibfritz, 16.09.2003
    #        Data matrices unscaled in Sec12_2.m (in directory above)
    #        cf. page 472
    # ------------------------------------------------------------------
    elif strmatch('HE4', ex, 'exact'):
        nx = 8
        nu = 4
        ny = 6
        a01 = np.array([[0, 0, 0, 0.99857378005981], [0, 0, 1.0, - 0.0031822193414],
                        [0, 0, - 11.5704956054688, - 2.54463768005371], [0, 0, 0.43935656547546, - 1.99818229675293],
                        [0, 0, - 2.04089546203613, - 0.4589991569519],
                        [- 32.1036071777344, 0, - 0.50335502624512, 2.29785919189453],
                        [0.10216116905212, 32.0578308105469, - 2.34721755981445, - 0.50361156463623],
                        [- 1.91097259521484, 1.71382904052734, - 0.00400543212891, - 0.05741119384766]])
        a02 = np.array([[0.05338427424431, 0, 0, 0], [0.0595246553421, 0, 0, 0],
                        [- 0.0636026263237, 0.10678052902222, - 0.09491866827011, 0.00710757449269],
                        [0, 0.01665188372135, 0.01846204698086, - 0.00118747074157],
                        [- 0.73502779006958, 0.01925575733185, - 0.00459562242031, 0.00212036073208],
                        [0, - 0.0212158113718, - 0.02116791903973, 0.01581159234047],
                        [0.83494758605957, 0.02122657001019, - 0.0378797352314, 0.00035400385968],
                        [0, 0.01398963481188, - 0.00090675335377, - 0.29051351547241]])
        A = np.hstack([a01, a02])
        B1 = np.eye(8)
        B = np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0.12433505058289, 0.08278584480286, - 2.75247764587402, - 0.01788876950741],
             [- 0.03635892271996, 0.47509527206421, 0.01429074257612, 0],
             [0.30449151992798, 0.01495801657438, - 0.49651837348938, - 0.20674192905426],
             [0.28773546218872, - 0.54450607299805, - 0.01637935638428, 0],
             [- 0.01907348632812, 0.01636743545532, - 0.54453611373901, 0.23484230041504],
             [- 4.82063293457031, - 0.00038146972656, 0, 0]])
        # C1 = np.array([[np.eye(8)], [np.zeros((4, 8))]])
        D11 = np.zeros((12, 8))
        # D12 = np.array([[np.zeros((8, 4))], [np.eye(4)]])
        C = np.array([[0, 0, 0, 0, 0, 0.0595, 0.05329, - 0.9968], [1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, - 0.05348, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0]])
        D21 = np.zeros((6, 8))


    # ------------------------------------------------------------------
    # (HE5): A variation of the system above with eight state, two
    #        measurement and four control variables. The matrices A and B
    #        are the same as in (HE4).
    # ------------------------------------------------------------------
    elif strmatch('HE5', ex, 'exact'):
        nx = 8
        nu = 4
        ny = 2
        nz = 4
        nw = 3
        a01 = np.array([[0, 0, 0, 0.99857378005981], [0, 0, 1.0, - 0.0031822193414],
                        [0, 0, - 11.5704956054688, - 2.54463768005371], [0, 0, 0.43935656547546, - 1.99818229675293],
                        [0, 0, - 2.04089546203613, - 0.4589991569519],
                        [- 32.1036071777344, 0, - 0.50335502624512, 2.29785919189453],
                        [0.10216116905212, 32.0578308105469, - 2.34721755981445, - 0.50361156463623],
                        [- 1.91097259521484, 1.71382904052734, - 0.00400543212891, - 0.05741119384766]])
        a02 = np.array([[0.05338427424431, 0, 0, 0], [0.0595246553421, 0, 0, 0],
                        [- 0.0636026263237, 0.10678052902222, - 0.09491866827011, 0.00710757449269],
                        [0, 0.01665188372135, 0.01846204698086, - 0.00118747074157],
                        [- 0.73502779006958, 0.01925575733185, - 0.00459562242031, 0.00212036073208],
                        [0, - 0.0212158113718, - 0.02116791903973, 0.01581159234047],
                        [0.83494758605957, 0.02122657001019, - 0.0378797352314, 0.00035400385968],
                        [0, 0.01398963481188, - 0.00090675335377, - 0.29051351547241]])
        A = np.hstack([a01, a02])
        B1 = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
        B = np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0.12433505058289, 0.08278584480286, - 2.75247764587402, - 0.01788876950741],
             [- 0.03635892271996, 0.47509527206421, 0.01429074257612, 0],
             [0.30449151992798, 0.01495801657438, - 0.49651837348938, - 0.20674192905426],
             [0.28773546218872, - 0.54450607299805, - 0.01637935638428, 0],
             [- 0.01907348632812, 0.01636743545532, - 0.54453611373901, 0.23484230041504],
             [- 4.82063293457031, - 0.00038146972656, 0, 0]])
        C1 = np.array(
            [[0, 0, 0, 0, 0, 0.0595, 0.05329, - 0.9968], [1.0, 0, 0, 0, 0, 0, 0, 0], [0, 1.0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, - 0.05348, 1.0, 0, 0, 0]])
        D11 = np.zeros((4, 3))
        D12 = np.eye(nu)
        C = np.array([[0, 0, 1.0, 0, 0, 0, 0, 0], [0, 0, 0, 1.0, 0, 0, 0, 0]])
        D21 = np.array([[0.01, 0, 0], [0, 0.01, 0]])


    # ------------------------------------------------------------------
    # (REA1): The Chemical Reactor Example    ##ehemals (CHR2)
    #         Y. S. Hung and A. G. J. MacFarlane, "Multivariable feedback:
    #         A  quasi-classical approach", Springer-Verlag,
    #         "Lecture Notes in Control and Information Sciences", 1982
    # ------------------------------------------------------------------
    elif strmatch('REA1', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 2
        A = np.array([[1.38, - 0.2077, 6.715, - 5.676], [- 0.5814, - 4.29, 0, 0.675], [1.067, 4.273, - 6.654, 5.893],
                      [0.048, 4.273, 1.343, - 2.104]])
        B = np.array([[0, 0], [5.679, 0], [1.136, - 3.146], [1.136, 0]])
        C = np.array([[1, 0, 1, - 1], [0, 1, 0, 0], [0, 0, 1, - 1]])


    # ------------------------------------------------------------------
    # (REA2): Obtained from (REA1) by leaving out the last row of the
    #         matrix C                                   ##ehemals (CHR1)
    # ------------------------------------------------------------------
    elif strmatch('REA2', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 3
        A = np.array([[1.4, - 0.208, 6.715, - 5.676], [- 0.581, - 4.29, 0, 0.675], [1.067, 4.273, - 6.654, 5.893],
                      [0.048, 4.273, 1.343, - 2.104]])
        B = np.array([[0, 0], [5.679, 0], [1.136, - 3.146], [1.136, 0]])
        C = np.array([[1, 0, 1, - 1], [0, 1, 0, 0]])


    # ------------------------------------------------------------------
    # (REA3): Nuclear reactor model, L. F. Miller, R. G. Cochran, J. W. Howze
    #         "Computation of Optimal Output Feedback Gains for Linear
    #         Multivariable Systems", TOAC, Vol. 19, pp. 257--258, 1974
    # ------------------------------------------------------------------
    elif strmatch('REA3', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 3
        A = np.array(
            [[- 0.4044, 0, 0, 0.4044, 0, 0, 0, 0, 0, 0, 0, 0], [0, - 0.4044, 0, 0, 0.4044, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, - 0.4044, 0, 0, 0.4044, 0, 0, 0, 0, 0, 0], [0.01818, 0, 0, - 0.5363, 0, 0, 0.4045, 0, 0, 0, 0, 0],
             [0, 0.0818, 0, 0.4545, - 0.5363, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0.0818, 0, 0.4545, - 0.5363, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0.15, 0, - 0.15, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, - 7.5, 0, 0, 75, 0, 0, 600, - 74.995, 0.033, 0.346, 0.621],
             [0, 0, 0, 0, 0, 0, 0, 0, 2.475, - 0.033, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 25.95, 0, - 0.346, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 46.57, 0, 0, - 0.621]])
        B = np.array([[0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0]])
        C = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])


    # ------------------------------------------------------------------
    # (REA4): Chemical reactor model by P. M. Maekilae, "Parametric LQ
    #         Control", IJOC, Vol. 41, Nr. 6, pp. 1413-1428, 1985
    #         (discrete modell)
    # ------------------------------------------------------------------
    elif strmatch('REA4', ex, 'exact'):
        nx = 8
        nu = 1
        ny = 1
        A = np.array([[0.5623, - 0.01642, 0.01287, - 0.0161, 0.02094, - 0.02988, 0.0183, 0.008743],
                      [0.102, 0.6114, - 0.02468, 0.02468, - 0.03005, 0.04195, - 0.02559, 0.03889],
                      [0.1361, 0.2523, 0.641, - 0.03404, 0.03292, - 0.04296, 0.02588, 0.08467],
                      [0.09951, 0.2859, 0.3476, 0.6457, - 0.03249, 0.03316, - 0.01913, 0.1103],
                      [- 0.04794, 0.08708, 0.3297, 0.3102, 0.6201, - 0.03015, 0.01547, 0.08457],
                      [- 0.1373, - 0.1224, 0.1705, 0.3106, 0.191, 0.5815, - 0.01274, 0.05394],
                      [- 0.1497, - 0.1692, 0.1165, 0.2962, 0.1979, 0.07631, 0.5242, 0.04702],
                      [0, 0, 0, 0, 0, 0, 0, 0.6065]])
        B = np.array([[- 0.1774], [- 0.2156], [- 0.2194], [- 0.09543], [0.0579], [0.09303], [0.08962], [0]])
        C = np.array([- 0.0049, 0.0049, - 0.006, 0.01, 0.0263, 0.3416, 0.6759, 0])
        B1 = np.array([[0], [0], [0], [0], [0], [0], [0], [1]])
        C1 = np.array([- 0.0465, - 0.1135, - 0.1909, - 0.2619, - 0.2634, - 0.1422, - 0.0002, 0.1856])
        D12 = np.array([0.1001])
        D11 = np.array([0])
        D21 = np.array([1])


    # ------------------------------------------------------------------
    # (DIS1): Decentralized Interconnected System;
    #         H. Singh, R. H. Brown and D. S. Naidu, "Unified approach to
    #         linear quadrtic regulator with time-scale property",
    #         Optimal Control Applications and Methods, Vol.22, pp.1-16, 2001
    # ------------------------------------------------------------------
    elif strmatch('DIS1', ex, 'exact'):
        A11 = np.array([[0.144, - 0.058, 0.056, 0.042], [- 0.506, - 0.236, - 0.02, - 0.012], [0, 0, - 0.278, 0.291],
                        [0, 0, 0, - 0.33]])
        A12 = np.array([[0.12, 2.1454, 0, 0.08], [- 0.06, - 0.909, 1.093, - 0.04], [0, 0, 0, 0.58], [0, 0, 0, 0]])
        A21 = np.array([[0, 0, 0.303, 0.029], [- 0.154, 0.133, - 0.006, - 0.004], [- 0.345, 0.304, - 0.018, - 0.014],
                        [0, 0, 0, 0.247]])
        A22 = np.array([[- 1.67, 0, 0, 0.092], [- 0.014, - 1.688, 0.236, 0.013], [- 0.032, - 0.611, - 1.824, - 0.024],
                        [0, 0, 0, - 1.978]])
        A = np.block([[A11, A12], [A21, A22]])
        Bb1 = np.array([[- 0.076, 0.02], [0.588, - 0.006], [0, 0.152], [0, 1.45]])
        Bb2 = np.array([[0, 0.012], [0.162, - 0.002], [0.414, - 0.008], [0, 0.248]])
        B = np.block([[Bb1, np.zeros((4, 2))], [np.zeros((4, 2)), Bb2]])
        Ch = np.eye(8)

        # C1 = np.array([[C], [np.zeros((4, 8))]])
        B1 = np.array([[1], [0], [1], [0], [1], [0], [1], [0]])
        D11 = np.zeros((8, 1))
        # D12 = np.array([[np.zeros((4, 4))], [np.eye(4)]])
        D21 = np.zeros((4, 1))


    # ------------------------------------------------------------------
    # (DIS2): Decentralized system with 2 control stations
    #         W. Q. Liu and V. Sreeram, "New Algorithm for Computing LQ
    #         Suboptimal Output Feedback Gains of Decentralized Control
    #         Systems", JOTA, Vol. 93
    # ------------------------------------------------------------------
    elif strmatch('DIS2', ex, 'exact'):
        A = np.array([[- 4, 2, 1], [3, - 2, 5], [- 7, 0, 3]])
        Bb1 = np.array([[1], [1], [0]])
        Bb2 = np.array([[0], [0], [1]])
        B = np.block([Bb1, Bb2])
        Cc1 = np.array([0, 1, 0])
        Cc2 = np.array([0, 0, 1])
        C = np.block([[Cc1], [Cc2]])


    # ------------------------------------------------------------------
    # (DIS3): M. Saif and Y. Guan,"Decentralized State Estimation in
    #         Large-Scale Interconnected Dynamical Systems",
    #         AUTO, Vol. 28, Nr. 1, pp. 215-219
    # ------------------------------------------------------------------
    elif strmatch('DIS3', ex, 'exact'):
        A = np.array(
            [[- 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [- 1.0, 1.0, 1.0, 0.0, 0.0, 0.0], [1.0, - 2.0, - 1.0, - 1.0, 1.0, 1.0],
             [0.0, 0.0, 0.0, - 1.0, 0.0, 0.0], [- 8.0, 1.0, - 1.0, - 1.0, - 2.0, 0.0],
             [4.0, - 0.5, 0.5, 0.0, 0.0, - 4.0]])
        B = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, - 1], [0, 0, 1, 0], [0, 0, 0, 1]])
        C = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])


    # ------------------------------------------------------------------
    # (DIS4): H. T. Toivonen and P. M. Maekilae, "A descent Anderson-
    #         Moore algorithm for optimal decentralized control",
    #         AUTO, Vol. 21, Nr. 6, pp.743-744, 1985
    # ------------------------------------------------------------------
    elif strmatch('DIS4', ex, 'exact'):
        A = np.array([[0, 1, 0.5, 1, 0.6, 0], [- 2, - 3, 1, 0, 0, 1], [0, 2, 0.5, 1, 1, 0.5], [1, 3, 0, 0.5, 0, - 0.5],
                      [0, 1, 1, 0, 1, 0], [- 3, - 4, 0, 0.5, 0.5, 0]])
        B = np.array([[1, 0, 0, 0], [1, 0, 0, 0], [0, 3, 0, 0], [0, 0, 4, 0], [0, 0, 0, 2], [0, 0, 0, 3]])
        C = np.array(
            [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1]])


    # ------------------------------------------------------------------
    # (DIS5): M. C. de Oliveira, J. F. Camino and R. E. Skelton,
    #         A Convexifying Algorithm of Structured Linear Controllers
    #         Tech. Report, FAPESP and CAPES, Brazil
    #         (discrete model)
    # ------------------------------------------------------------------
    elif strmatch('DIS5', ex, 'exact'):
        A = np.array(
            [[0.8189, 0.0863, 0.09, 0.0813], [0.2524, 1.0033, 0.0313, 0.2004], [- 0.0545, 0.0102, 0.7901, - 0.258],
             [- 0.1918, - 0.1034, 0.1602, 0.8604]])
        B = np.array([[0.0045, 0.0044], [0.1001, 0.01], [0.0003, - 0.0136], [- 0.0051, 0.0936]])
        C = np.array([[1, 0, 0, 0], [0, 0, 1, 0]])
        B1 = np.array([[0.0953, 0, 0], [0.0145, 0, 0], [0.0862, 0, 0], [- 0.0011, 0, 0]])
        C1 = np.array([[1, 0, - 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        D11 = np.zeros((3, 3))
        D12 = np.array([[0, 0], [1, 0], [0, 1]])
        D21 = np.array([[0, 1, 0], [0, 0, 1]])


    # ------------------------------------------------------------------
    # (TG1): Turbo-Generator
    #        Y. S. Hung and A. G. J. MacFarlane, "Multivariable feedback:
    #        A  quasi-classical approach", Springer-Verlag,
    #        "Lecture Notes in Control and Information Sciences", 1982
    #        p. 117/167
    # ------------------------------------------------------------------
    elif strmatch('TG1', ex, 'exact'):
        nx = 10
        nu = 2
        ny = 2
        A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, - 0.11323, - 0.98109, - 11.847, - 11.847, - 63.08, - 34.339, - 34.339, - 27.645, 0],
                      [324.121, - 1.1755, - 29.101, 0.12722, 2.83448, - 967.73, - 678.14, - 678.14, 0, - 129.29],
                      [- 127.3, 0.46167, 11.4294, - 1.0379, 13.1237, 380.079, 266.341, 266.341, 0, 1054.85],
                      [- 186.05, 0.67475, 16.7045, 0.86092, - 17.068, 555.502, 389.268, 389.268, 0, - 874.92],
                      [341.917, 1.09173, 1052.75, 756.465, 756.465, - 29.774, 0.16507, 3.27626, 0, 0],
                      [- 30.748, - 0.09817, - 94.674, - 68.029, - 68.029, 2.67753, - 2.6558, 4.88497, 0, 0],
                      [- 302.36, - 0.96543, - 930.96, - 668.95, - 668.95, 26.3292, 2.42028, - 9.5603, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, - 1.6667, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, - 10]])
        B = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1.6667, 0], [0, 10]])
        C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [- 0.49134, 0, - 0.63203, 0, 0, - 0.20743, 0, 0, 0, 0]])


    # ------------------------------------------------------------------
    # (AGS): Automobile Gas Turbine
    #        Y. S. Hung and A. G. J. MacFarlane, "Multivariable feedback:
    #        A  quasi-classical approach", Springer-Verlag,
    #        "Lecture Notes in Control and Information Sciences", 1982
    #        p. 27/163
    # ------------------------------------------------------------------
    elif strmatch('AGS', ex, 'exact'):
        nx = 12
        nu = 2
        ny = 2
        A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [- 0.202, - 1.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, - 2.36, - 13.6, - 12.8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, - 1.62, - 9.4, - 9.15, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, - 188, - 111.6, - 116.4, - 20.8]])
        B = np.array(
            [[0, 0], [1.0439, 4.1486], [0, 0], [0, 0], [- 1.794, 2.6775], [0, 0], [0, 0], [1.0439, 4.1486], [0, 0],
             [0, 0], [0, 0], [- 1.794, 2.6775]])
        C = np.array([[0.264, 0.806, - 1.42, - 15, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 4.9, 2.12, 1.95, 9.35, 25.8, 7.14, 0]])


    # ------------------------------------------------------------------
    # (BDT1): Binary distillation tower with pressure variation
    #         E. J. Davison, "Benchmark Problems for Control System Design",
    #         "Report of the IFAC Theory Comittee", 1990
    # ------------------------------------------------------------------
    elif strmatch('BDT1', ex, 'exact'):
        nx = 11
        nu = 3
        ny = 3
        A = np.array(
            [[- 0.014, 0.0043, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.0095, - 0.0138, 0.0046, 0, 0, 0, 0, 0, 0, 0, 0.0005],
             [0, 0.0095, - 0.0141, 0.0063, 0, 0, 0, 0, 0, 0, 0.0002], [0, 0, 0.0095, - 0.0158, 0.011, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0.0095, - 0.0312, 0.015, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0.0202, - 0.0352, 0.022, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0.0202, - 0.0422, 0.028, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0.0202, - 0.0482, 0.037, 0, 0.0002],
             [0, 0, 0, 0, 0, 0, 0, 0.0202, - 0.0572, 0.042, 0.0005], [0, 0, 0, 0, 0, 0, 0, 0, 0.0202, - 0.0483, 0.0005],
             [0.0255, 0, 0, 0, 0, 0, 0, 0, 0, 0.0255, - 0.0185]])
        B = np.array(
            [[0, 0, 0], [5e-06, - 4e-05, 0.0025], [2e-06, - 2e-05, 0.005], [1e-06, - 1e-05, 0.005], [0, 0, 0.005],
             [0, 0, 0.005], [- 5e-06, 1e-05, 0.005], [- 1e-05, 3e-05, 0.005], [- 4e-05, 5e-06, 0.0025],
             [- 2e-05, 2e-06, 0.0025], [0.00046, 0.00046, 0]])
        C = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
        B1 = np.zeros((11, 1))
        B1[4, 0] = 0.01
        C1 = np.block([[C], [np.zeros((3, nx))]])
        nx, nw = B1.shape
        nz, nx = C1.shape
        D12 = np.block([[np.zeros((nz - nu, nu))], [np.eye(nu)]])
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # ------------------------------------------------------------------
    # (MFP): Moored Floating Platform
    #        C. Scherer, P. Gahinet and M. Chilali, "Multiobjective Output-
    #        Feedback Control via LMI Optimization",
    #        TOAC, Vol. 42, Nr. 7, pp. 896-911, 1997
    # ------------------------------------------------------------------
    elif strmatch('MFP', ex, 'exact'):
        nx = 4
        nu = 3
        ny = 2
        A = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [- 0.101, - 0.1681, - 0.04564, - 0.01075],
                      [0.06082, - 2.1407, - 0.05578, - 0.1273]])
        B = np.array([[0, 0, 0], [0, 0, 0], [0.1179, 0.1441, 0.1476], [0.1441, 1.7057, - 0.7557]])
        C = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])



    # ------------------------------------------------------------------
    # (UWV): Control surface servo for an underwater vehicle,
    #         E. J. Davison, "Benchmark Problems for Control System Design",
    #         "Report of the IFAC Theory Comittee", 1990; p.32
    # ------------------------------------------------------------------
    elif strmatch('UWV', ex, 'exact'):
        nx = 8
        nu = 2
        ny = 2
        nw = 2
        nz = 1
        A = np.array(
            [[0, 850, 0, 0, 0, 0, 0, 0], [- 850, - 120, - 4100, 0, 0, 0, 0, 0], [33, 0, - 33, 0, - 700, 0, 0, 0],
             [0, 0, 0, 0, 1400, 0, 0, 0], [0, 0, 1600, - 450, - 110, 0, 0, 0], [0, 0, 0, 81, 0, - 1, 0, - 900],
             [0, 0, 0, 0, 0, 0, 0, 110], [0, 0, 0, 0, 0, 12, - 1.1, - 22]])
        B = np.array([[0, 0], [4.6, 99000], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
        C = np.array([[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]])
        B1 = np.array([[0, 0], [9900, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 99]])
        C1 = np.array([0, 0, 0, 0, 0, 0, 1, 0])
        D12 = np.array([1, 0])
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # ------------------------------------------------------------------
    # (EB1): Euler-Bernoulli Beam; J. C. Geromel and P. B. Gapski
    #        "Synthesis of positive real H2 controllers"
    #	 TOAC, Vol. 42, Nr. 7, pp. 988-992, 1997
    #        low damping --> xi=1e-2
    #        s_max=5 --> nx=10
    # ------------------------------------------------------------------
    elif strmatch('EB1', ex, 'exact'):
        nx = 10
        nu = 1
        ny = 1
        O = np.zeros((2, 2))
        xi = 0.01
        s = 1
        w = s ** 2
        A1 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 2
        w = s ** 2
        A2 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 3
        w = s ** 2
        A3 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 4
        w = s ** 2
        A4 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 5
        w = s ** 2
        A5 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        A = np.block([[A1, O, O, O, O], [O, A2, O, O, O], [O, O, A3, O, O], [O, O, O, A4, O], [O, O, O, O, A5]])
        B = np.array([[0], [0.9877], [0], [- 0.309], [0], [- 0.891], [0], [0.5878], [0], [0.7071]])
        C = np.transpose(B)
        B1 = np.array(
            [[0, 0], [0.9877, 0], [0, 0], [- 0.309, 0], [0, 0], [- 0.891, 0], [0, 0], [0.5878, 0], [0, 0], [0.7071, 0]])
        C1 = np.array([[0, 0.809, 0, - 0.9511, 0, 0.309, 0, 0.5878, 0, - 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        D12 = np.array([[0], [1.9]])
        D21 = np.array([0, 1.9])
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))

    # ------------------------------------------------------------------
    # (EB2): Euler-Bernoulli Beam; like (EB1) with changed performance
    #        criteria, (-> C1, D12)
    #        low damping --> xi=1e-2
    #        s_max=5 --> nx=10
    # ------------------------------------------------------------------
    elif strmatch('EB2', ex, 'exact'):
        nx = 10
        nu = 1
        ny = 1
        O = np.zeros((2, 2))
        xi = 0.01
        s = 1
        w = s ** 2
        A1 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 2
        w = s ** 2
        A2 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 3
        w = s ** 2
        A3 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 4
        w = s ** 2
        A4 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        s = 5
        w = s ** 2
        A5 = np.array([[0, 1], [- w ** 2, - 2 * xi * w]])
        A = np.block([[A1, O, O, O, O], [O, A2, O, O, O], [O, O, A3, O, O], [O, O, O, A4, O], [O, O, O, O, A5]])
        B = np.array([[0], [0.9877], [0], [- 0.309], [0], [- 0.891], [0], [0.5878], [0], [0.7071]])
        C = np.transpose(B)
        B1 = np.array(
            [[0, 0], [0.9877, 0], [0, 0], [- 0.309, 0], [0, 0], [- 0.891, 0], [0, 0], [0.5878, 0], [0, 0], [0.7071, 0]])
        C1 = np.array([[0.809, 0, - 0.9511, 0, 0.309, 0, 0.5878, 0, - 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        D12 = np.array([[0], [0.5]])
        D21 = np.array([0, 1.9])
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))


    # ------------------------------------------------------------------
    # (PAS): Piezoelectric actuator system
    #        B. M. Chen, "H_inf Control and Its Applications",
    #        Springer-Verlag, "Lecture Notes in Control and Information Sciences",
    #        Vol.235, 1998; p.283
    # ------------------------------------------------------------------
    elif strmatch('PAS', ex, 'exact'):
        nx = 5
        nu = 1
        ny = 3
        A = np.array(
            [[0, 1, 0, 0, 0], [- 274921.63, - 73.2915, - 274921.63, 0, 0], [0, 0, - 0.9597, 0, 0], [1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]])
        B = np.array([[0], [0.12841], [- 3.39561e-07], [0], [0]])
        C = np.array([[1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
        B1 = np.array([[0, 0], [- 274921.63, 0], [0, 0], [0, - 1], [0, 0]])
        # C1 = np.array([0, 0, 0, 0, 1])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))
        # D12 = np.zeros((nz, nu))
        # D21 = np.zeros((ny, nw))


    # ------------------------------------------------------------------
    # (TF1): Terrain following model
    #       Gershon, Shaked, Yaesh, Tech.-Rep. 2003 (Uni. Tel-Aviv)
    #       "Static output feedback of state multiplicative systems with
    #       application to terrain following"
    # Note: This is not a classical SOF control design --> special ROC
    # Q: Is the problem SOF stabilizable too ?
    # ------------------------------------------------------------------
    elif strmatch('TF1', ex, 'exact'):
        beta = 1 / 20
        eps2 = - 1e-05
        A = np.array([[- 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, - 1, 0, 0], [- 0.088, 0.0345, 0, 0, 1, - 0.0032, 0], [0, 0, beta, 0, 0, 0, eps2]])
        B = np.array([[1, 0], [0, 0], [0, 0], [0, 0.09], [0, 0], [0, 0], [0, 0]])
        C = np.array([[0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0]])
        B1 = np.array([[0], [0], [0], [0], [0], [0], [- beta]])
        # C1 = np.zeros((4, 7))
        # C1[1, 7] = 1.0
        # C1[2, 6] = 2.23
        D11 = np.zeros((4, 1))
        D12 = np.block([[np.zeros((2, 2))], [np.sqrt(3), 0], [0, np.sqrt(0.3)]])
        D21 = np.array([[0.04], [0], [0], [0]])


    # ------------------------------------------------------------------
    # (TF2): Like (TF1) with a different sensor matrix C.
    # ------------------------------------------------------------------
    elif strmatch('TF2', ex, 'exact'):
        beta = 1 / 20
        eps2 = - 1e-05
        A = np.array([[- 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, - 1, 0, 0], [- 0.088, 0.0345, 0, 0, 1, - 0.0032, 0], [0, 0, beta, 0, 0, 0, eps2]])
        B = np.array([[1, 0], [0, 0], [0, 0], [0, 0.09], [0, 0], [0, 0], [0, 0]])
        C = np.array([[0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]])
        B1 = np.array([[0], [0], [0], [0], [0], [0], [- beta]])
        # C1 = np.zeros((4, 7))
        # C1[1, 7] = 1.0
        # C1[2, 6] = 2.23
        D11 = np.zeros((4, 1))
        D12 = np.block([[np.zeros((2, 2))], [np.sqrt(3), 0], [0, np.sqrt(0.3)]])
        D21 = np.array([[0.04], [0], [0]])


    # ------------------------------------------------------------------
    # (TF3): Another sensor matrix $C$ for the terrain following model.
    # ------------------------------------------------------------------
    elif strmatch('TF3', ex, 'exact'):
        beta = 1 / 20
        eps2 = - 1e-05
        A = np.array([[- 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, - 1, 0, 0], [- 0.088, 0.0345, 0, 0, 1, - 0.0032, 0], [0, 0, beta, 0, 0, 0, eps2]])
        B = np.array([[1, 0], [0, 0], [0, 0], [0, 0.09], [0, 0], [0, 0], [0, 0]])
        C = np.array([[0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]])
        B1 = np.array([[0], [0], [0], [0], [0], [0], [- beta]])
        # C1 = np.zeros((4, 7))
        # C1[1, 7] = 1.0
        # C1[2, 6] = 2.23
        D11 = np.zeros((4, 1))
        D12 = np.block([[np.zeros((2, 2))], [np.sqrt(3), 0], [0, np.sqrt(0.3)]])
        D21 = np.array([[0.04], [0], [0]])


    # ------------------------------------------------------------------
    # (PSM): Power system model
    #        A. Varga, "Model Reduction Routines for {SLICOT}",
    #        NICONET Report 1999-8, p. 32
    #        and
    #        C. E. Fosha and O. I. Elgerd,"The megawatt-frequency control
    #        problem: a new approach via optimal control theory",
    #        IEEE Trans. on Power Apparatus and Systems,Vol.89,pp.563-571,1970
    # ------------------------------------------------------------------
    elif strmatch('PSM', ex, 'exact'):
        nx = 7
        nu = 2
        ny = 3
        A = np.array(
            [[- 0.04165, 0, 4.92, - 4.92, 0, 0, 0], [- 5.21, - 12.5, 0, 0, 0, 0, 0], [0, 3.33, - 3.33, 0, 0, 0, 0],
             [0.545, 0, 0, 0, - 0.545, 0, 0], [0, 0, 0, 4.92, - 0.04165, 0, 4.92], [0, 0, 0, 0, - 5.21, - 12.5, 0],
             [0, 0, 0, 0, 0, 3.33, - 3.33]])
        B = np.array([[- 4.92, 0], [0, 0], [0, 0], [0, 0], [0, - 4.92], [0, 0], [0, 0]])
        C = np.array([[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]])
        B1 = np.array([[0, 0], [12.5, 0], [0, 0], [0, 0], [0, 0], [0, 12.5], [0, 0]])
        C1 = np.block([[C], [np.zeros((2, 7))]])
        D12 = np.block([[np.zeros((3, 2))], [np.eye(2)]])
        nz, nx = C1.shape
        nx, nw = B1.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # --------------------------------------------------------------------
    # (NN1): L. F. Miller, R. G. Cochran and J. W. Howze,
    #        "Output feedback stabilization of a spectral radius functional",
    #        IJOC, Vol. 27, pp. 455-462, 1978
    # --------------------------------------------------------------------
    elif strmatch('NN1', ex, 'exact'):
        nx = 3
        nu = 1
        ny = 2
        A = np.array([[0, 1, 0], [0, 0, 1], [0, 13, 0]])
        B = np.array([[0], [0], [1]])
        C = np.array([[0, 5, - 1], [- 1, - 1, 0]])


    # --------------------------------------------------------------------
    # (NN2): Classical example
    #        W. S. Levine and M. Athans, "On the determination of the optimal
    #        constant output feedback gains for linear multivariable systems",
    #        TOAC, Vol. 15, Nr. 8, pp. 44-48
    # --------------------------------------------------------------------
    elif strmatch('NN2', ex, 'exact'):
        A = np.array([[0, 1], [- 1, 0]])
        B1 = np.array([[1, 0], [0, 1]])
        B = np.array([[0], [1]])
        C1 = np.array([[1, 0], [0, 0]])
        # C = np.array([0, 1])
        # nx, nx = A.shape
        # nx, nw = B1.shape
        # nx, nu = B.shape
        # nz, nx = C1.shape
        # ny, nx = C.shape
        # D11 = np.zeros((nz, nw))
        # D21 = np.zeros((ny, nw))
        # D12 = np.array([[0], [1]])


    # --------------------------------------------------------------------
    # (NN3): C. W. Scherer, "An Efficient Solution to Multi--Objective
    #        Control Problems with LMI Objectives",
    #        Delft University of Technology, The Netherlands, 2000
    # --------------------------------------------------------------------
    elif strmatch('NN3', ex, 'exact'):
        A = np.array([[0.5, 1, 1.5, 1], [- 1, 3, 2.1, 2], [1, - 1, - 0.6, 1], [- 2, 2, - 1, 1]])
        B1 = np.array([[0], [0], [1], [0]])
        B = np.array([[0], [0], [0], [1]])
        C1 = np.array([1, 0, 0, 0])
        # C = np.array([0, 0, 0, 1])
        # D12 = np.array([0])
        # nx, nx = A.shape
        # nx, nu = B.shape
        # ny, nx = C.shape
        # nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))
        # D21 = np.zeros((ny, nw))


    # --------------------------------------------------------------------
    # (NN4): L. F. Miller, R. G. Cochran and J. W. Howze,
    #        "Output feedback stabilization of a spectral radius functional",
    #        IJOC, Vol. 27, pp. 455-462, 1978
    # --------------------------------------------------------------------
    elif strmatch('NN4', ex, 'exact'):
        nx = 4
        nu = 2
        ny = 3
        A = np.array([[0, 1, 0, 0], [0, - 2.93, - 4.75, - 0.78], [0.086, 0, - 0.11, - 1], [0, - 0.042, 2.59, - 0.39]])
        B = np.array([[0, 0], [0, - 3.91], [0.035, 0], [- 2.53, 0.31]])
        C = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])


    # --------------------------------------------------------------------
    # (NN5): Saturn V booster
    #        L. F. Miller, R. G. Cochran and J. W. Howze,
    #        "Output feedback stabilization of a spectral radius functional",
    #        IJOC, Vol. 27, pp. 455-462, 1978
    # --------------------------------------------------------------------
    elif strmatch('NN5', ex, 'exact'):
        nx = 7
        nu = 1
        ny = 2
        A = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 0, 0.2, - 0.65, - 0.002, 2.6, 0],
                      [- 0.014, 1, - 0.041, 0.0002, - 0.015, - 0.033, 0], [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, - 45, - 0.13, 255, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, - 50, - 10]])
        B = np.array([[0], [0], [0], [0], [0], [0], [1]])
        C = np.array([[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]])


    # --------------------------------------------------------------------
    # (NN6): H. P. Horisberger and P. R. Belanger, "Solution of the Optimal
    #        Constant Output Feedback Problem by Conjugate Gradients",
    #        TOAC, Vol. 19, pp. 434-435, 1974   ###ehemals (HB1)
    # --------------------------------------------------------------------
    elif strmatch('NN6', ex, 'exact'):
        nx = 9
        nu = 1
        ny = 4
        A = np.array(
            [[0, 1, 0, 0, 0, 0, 0, 0, 0], [0, - 20, - 4.2, 0, 4.45, 12.5, 0, 100, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 4.7, 8.35, 0, - 1.1, 0, 0, 0, 0], [0, 0, 0, 0, - 3.3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 10.9, 0, 0, - 2.55, - 250, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 5.9, 0, 0, - 1.39, 0, 0, - 3700, 0]])
        B = np.array([[0], [0], [0], [0], [3.3], [0], [0], [0], [0]])
        C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0.66, 0, 1.2, 0],
                      [0, 0, 0, 1, 0, 0, 0.66, 0, 1.2]])
        B1 = np.sqrt(0.1) * np.eye(nx)
        C1 = np.sqrt(10) * np.eye(nx)
        nz, nx = C1.shape
        nx, nw = B1.shape
        # D12 = 10 * np.array([[np.zeros((nz - nu, nu))], [np.eye(nu)]])
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # --------------------------------------------------------------------
    # (NN7): like (NN6) with changed B1, C1, D11, D12 and D21 ###ehemals (HB2)
    # --------------------------------------------------------------------
    elif strmatch('NN7', ex, 'exact'):
        nx = 9
        nu = 1
        ny = 4
        A = np.array(
            [[0, 1, 0, 0, 0, 0, 0, 0, 0], [0, - 20, - 4.2, 0, 4.45, 12.5, 0, 100, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 4.7, 8.35, 0, - 1.1, 0, 0, 0, 0], [0, 0, 0, 0, - 3.3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 10.9, 0, 0, - 2.55, - 250, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 5.9, 0, 0, - 1.39, 0, 0, - 3700, 0]])
        B = np.array([[0], [0], [0], [0], [3.3], [0], [0], [0], [0]])
        C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0.66, 0, 1.2, 0],
                      [0, 0, 0, 1, 0, 0, 0.66, 0, 1.2]])
        B1 = np.array(
            [[0.145, 0.478, 0, 0, 0], [0, 0, 0, - 1, 0], [0.0523, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 0.598, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
        C1 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        D12 = np.array([[0], [0], [1]])
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))


    # --------------------------------------------------------------------
    # (NN8)
    # --------------------------------------------------------------------
    elif strmatch('NN8', ex, 'exact'):
        nx = 3
        nu = 2
        ny = 2
        A = np.array([[- 0.2, 0.1, 1], [- 0.05, 0, 0], [0, 0, - 1]])
        B = np.array([[0, 1], [0, 0.7], [1, 0]])
        C = np.array([[1, 0, 0], [0, 1, 0]])


    # --------------------------------------------------------------------
    # (NN9): B. M. Chen, "H_inf Control and Its Applications",
    #        Springer-Verlag, "Lecture Notes in Control and Information Sciences",
    #        Vol.235, 1998; p. 110
    # --------------------------------------------------------------------
    elif strmatch('NN9', ex, 'exact'):
        nx = 5
        nu = 3
        ny = 2
        A = np.array([[1, 1, 1, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]])
        B = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]])
        C = np.array([[0, - 2, - 3, - 2, - 1], [1, 2, 3, 2, 1]])
        B1 = np.array([[5, 1], [0, 0], [0, 0], [2, 3], [1, 4]])
        C1 = np.array([[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
        D12 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
        D21 = np.array([[1, 0], [0, 0]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))


    # --------------------------------------------------------------------
    # (NN10): X. A. Wang, "Grassmannian, Central Projection, and Output
    #         Feedback Pole Assignment of Linear Systems", TOAC, Vol. 41,
    #         Nr. 6, pp. 786-794, 1996; Example 3.7
    # --------------------------------------------------------------------
    elif strmatch('NN10', ex, 'exact'):
        A = np.array([[0, - 1, 0, 0, 0, 0, 0, 1], [1, 2, 0, 0, 1, 0, 0, - 2], [0, - 1, 0, 0, 5, 0, 0, 0],
                      [0, 0, 1, 0, - 7, 0, 0, - 2], [0, - 1, 0, 1, 4, 0, 0, 2], [0, - 2, 0, 0, 2, 0, 0, 3],
                      [0, 0, 0, 0, - 1, 1, 0, - 2], [0, - 1, 0, 0, 1, 0, 1, - 1]])
        B = np.array(
            [[0, 1, 2], [1, 0, 1], [- 1, - 1, - 3], [1, 0, 1], [0, 2, 4], [2, 1, 5], [- 1, 1, 1], [1, - 1, - 1]])
        C = np.array([[0, 1, 0, 0, - 2, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]])
        B1 = np.zeros((8, 3))
        C1 = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D12 = np.zeros((nz, nu))
        D21 = np.zeros((ny, nw))



    # --------------------------------------------------------------------
    # (NN11): P. Apkarian and H. D. Tuan, "Robust Conrol via Concave
    #         Minimization, Local and Global Algorithms", TOAC, Vol. 45,
    #         Nr. 2, pp. 299-305, 2000
    # --------------------------------------------------------------------
    elif strmatch('NN11', ex, 'exact'):
        A1 = np.array(
            [[- 101, - 99.9, 0, 0, 0, 0, 0, 0], [0, - 101, 0, 0, 0, 0, 0, 0], [0, 0, - 101, - 99.9, 0, 0, 0, 0],
             [0, 0, 0, - 101, 0, 0, 0, 0], [0, 0, 0, 0, - 1, 0, 0, 0], [0, 0, 0, 0, 0, - 1, 0, 0],
             [0, 0, 0, 0, 0, 0, - 1, 0], [0, 0, 0, 0, 0, 0, 0, - 1], [0, 0, 0, 0, 0, 0, 427.098, - 46.8341],
             [0, 0, 0, 0, 0, 0, 232.0719, 120.4649], [0, 0, 0, 0, 0, 0, - 764.2456, 85.4154],
             [0, 0, 0, 0, 0, 0, 166.827, - 264.7739], [0, 0, 0, 0, 0.3162, 0, 0, 0], [0, 0, 0, 0, - 0.125, 0, 0, 0],
             [0, 0, 0, 0, 0, 0.3162, 0, 0], [0, 0, 0, 0, 0, - 0.125, 0, 0]])
        A2 = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
             [- 1, 0, 0.4271, - 0.0468, 0, 0, 0, 0], [0, - 1, 0.2321, 0.1205, 0, 0, 0, 0],
             [0, 0, - 1.7642, 0.0854, 0, 0, 0, 0], [0, 0, 0.1668, - 1.2648, 0, 0, 0, 0],
             [0, 0, 0, 0, - 1.1, - 0.0759, 0, 0], [0, 0, 0, 0, 0, - 1, 0, 0], [0, 0, 0, 0, 0, 0, - 1.1, - 0.0759],
             [0, 0, 0, 0, 0, 0, 0, - 1]])
        A = np.block([A1, A2])
        B = np.array(
            [[0, - 9.995, 0], [0.199, - 9.995, 0], [0.211, 0, - 9.995], [- 0.233, 0, - 9.995], [0, 0, 0], [0, 0, 0],
             [0, 0, 0], [0, 0, 0], [0, 2.7173, 1.4274], [0, 1.4274, 2.8382], [0, - 4.7909, - 2.6032],
             [0, 1.0261, - 2.6393], [0.11, 0, 0], [0, 0, 0], [0, 0, 0], [0.01, 0, 0]])
        C = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.3162, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.3162, 0],
                      [0, 0, 0, 0, 0, 0, 1.5564, 3.4834, 0, 0, 0.0016, 0.0035, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.4743, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.3479, 0]])
        B1 = np.array(
            [[0, - 0.001, 0], [0, - 0.001, 0], [0, 0, - 0.001], [0, 0, - 0.001], [0, 0, 0], [0, 0, 0], [0, 0, 0],
             [0, 0, 0], [0.1787, 0.0003, 0.0001], [- 0.8364, 0.0001, 0.0003], [0.0818, - 0.0005, - 0.0003],
             [0.3577, 0.0001, - 0.0003], [0, - 0.3162, 0], [0, 0.125, 0], [- 0.3162, 0, 0], [0, 0, 0.125]])
        C1 = np.array([[0, 0, 0, 0, 0, 0, 1.5564, 3.4834, 0, 0, 0.0016, 0.0035, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.4743, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, - 0.3479, 0]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D12 = np.zeros((nz, nu))
        D21 = np.zeros((ny, nw))


    # --------------------------------------------------------------------
    # (NN12): J. Rosenthal and X. A. Wang, "Output Feedback Pole Placement
    #         with Dynamic Compensators", TOAC, Vol. 41, Nr. 6,
    #         pp.830-843, 1996, Example 3.14
    # --------------------------------------------------------------------
    elif strmatch('NN12', ex, 'exact'):
        A = np.array(
            [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, - 1], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
             [0, 0, - 1, 0, 1, 0]])
        B = - np.array([[1, 3], [0, 0], [0, - 1], [0, 1], [0, 1], [0, 0]])
        C = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]])


    # --------------------------------------------------------------------
    # (NN13): D.-W. Gu, P. Hr. Petkov and M. M. Konstantinov,
    #         "H_inf and H_2 Optimization Toolbox in SLICOT",
    #         SLICOT Working note 1999-12, p. 15
    #         available via ftp: wgs.esat.kuleuven.ac.be/
    #                            pub/WGS/REPORTS/SLWN1999-12.ps.Z
    # --------------------------------------------------------------------
    elif strmatch('NN13', ex, 'exact'):
        A = np.array(
            [[- 1, 0, 4, 5, - 3, - 2], [- 2, 4, - 7, - 2, 0, 3], [- 6, 9, - 5, 0, 2, - 1], [- 8, 4, 7, - 1, - 3, 0],
             [2, 5, 8, - 9, 1, - 4], [3, - 5, 8, 0, 2, - 6]])
        B = np.array([[1, 0], [- 5, 2], [7, - 2], [1, - 2], [0, 5], [- 6, - 2]])
        C = np.array([[9, - 3, 4, 0, 3, 7], [0, 1, - 2, 1, - 6, - 2]])
        B1 = np.array([[- 3, - 4, - 2], [2, 0, 1], [- 5, - 7, 0], [4, - 6, 1], [- 3, 9, - 8], [1, - 2, 3]])
        C1 = np.array([[1, - 1, 2, - 4, 0, - 3], [- 3, 0, 5, - 1, 1, 1], [- 7, 5, 0, - 8, 2, - 2]])
        D11 = np.array([[1, - 2, - 3], [0, 4, 0], [5, - 3, - 4]])
        D12 = np.array([[0, 0], [1, 0], [0, 1]])
        D21 = np.array([[0, 1, 0], [0, 0, 1]])


    # --------------------------------------------------------------------
    # (NN14): D.-W. Gu, P. Hr. Petkov and M. M. Konstantinov,
    #         "H_inf and H_2 Optimization Toolbox in SLICOT",
    #         SLICOT Working note 1999-12, p. 19
    #         same as NN13, diff. D11, D12, D21
    #         available via ftp: wgs.esat.kuleuven.ac.be/
    #                            pub/WGS/REPORTS/SLWN1999-12.ps.Z
    # --------------------------------------------------------------------
    elif strmatch('NN14', ex, 'exact'):
        A = np.array(
            [[- 1, 0, 4, 5, - 3, - 2], [- 2, 4, - 7, - 2, 0, 3], [- 6, 9, - 5, 0, 2, - 1], [- 8, 4, 7, - 1, - 3, 0],
             [2, 5, 8, - 9, 1, - 4], [3, - 5, 8, 0, 2, - 6]])
        B = np.array([[1, 0], [- 5, 2], [7, - 2], [1, - 2], [0, 5], [- 6, - 2]])
        C = np.array([[9, - 3, 4, 0, 3, 7], [0, 1, - 2, 1, - 6, - 2]])
        B1 = np.array([[- 3, - 4, - 2], [2, 0, 1], [- 5, - 7, 0], [4, - 6, 1], [- 3, 9, - 8], [1, - 2, 3]])
        C1 = np.array([[1, - 1, 2, - 4, 0, - 3], [- 3, 0, 5, - 1, 1, 1], [- 7, 5, 0, - 8, 2, - 2]])
        D11 = np.zeros((3, 3))
        D12 = np.array([[- 4, - 1], [1, 0], [0, 1]])
        D21 = np.array([[3, 1, 0], [- 2, 0, 1]])


    # --------------------------------------------------------------------
    # (NN15): Space backpack model
    #         P. L. D. Peres and J. C. Geromel,
    #         "An Alternate Numerical Solution to the Linear Quadratic Problem",
    #         TOAC, Vol. 39, Nr. 1, pp. 198-202, 1994
    # --------------------------------------------------------------------
    elif strmatch('NN15', ex, 'exact'):
        A = np.array([[0, 1, 0], [- 79.285, - 0.113, 0], [28.564, 0.041, 0]])
        # B1=eye(size(A));
        B1 = np.array([[0], [0.041], [- 0.03]])
        B = np.array([[0, 0], [0.041, - 0.0047], [- 0.03, - 0.0016]])
        C1 = np.array([[0, 0, 1], [1, 0, 0], [0, 0, 0], [0, 0, 0]])
        C = np.array([[0, 0, 1], [1, 0, 0]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))
        D12 = np.array([[0, 0], [0, 0], [0.1, 0], [0, 0.1]])


    # ------------------------------------------------------------------
    # (NN16): Application for an large space structure
    #         A. J. Calise and D. D. Moerder, "Optimal Output Feedback
    #         Design of Systems with Ill-conditioned Dynamics",
    #         AUTO, Vol. 21, Nr. 3, pp. 271-276, 1985
    # ------------------------------------------------------------------
    elif strmatch('NN16', ex, 'exact'):
        nx = 8
        nu = 4
        ny = 4
        A = np.array([[0, 1, 0, 0, 0, 0, 0, 0], [- 0.42, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, - 0.1849, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, - 4.41, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, - 4.84, 0]])
        B = np.array([[0, 0, 0, 0], [- 0.92, - 1.4, 0.92, - 1.4], [0, 0, 0, 0], [0.65, 1.6, 0.65, - 1.6], [0, 0, 0, 0],
                      [1.4, - 1, 1.4, 1], [0, 0, 0, 0], [2, - 0.8, - 2, - 0.8]])
        C = np.array([[0, - 1.8, 0, 1.3, 0, 2.9, 0, 4.1], [0, - 2.7, 0, 3.2, 0, - 2.1, 0, - 1.6],
                      [0, 1.8, 0, 1.3, 0, 2.9, 0, - 4.1], [0, - 2.7, 0, - 3.2, 0, 2.1, 0, - 1.6]])
        C1 = np.zeros((4, 8))
        C1[1, 1] = 0.065
        C1[2, 2] = 0.065
        D12 = np.eye(4)
        B1 = np.eye(nx)
        D11 = np.zeros((4, 8))
        D21 = np.zeros((4, 8))


    # --------------------------------------------------------------------
    # (NN17): Rank-deficient matrix D12, P. Gahinet and A. J. Laub,
    #         "Numerically reliable computation of optimal performance in
    #         singular H_inf control", SIOPT, Vol. 35, Nr. 5,
    #         pp. 1690-1710, 1997
    # --------------------------------------------------------------------
    elif strmatch('NN17', ex, 'exact'):
        A = np.array([[0, - 1, 2], [1, - 2, 3], [0, 1, 0]])
        B1 = np.array([[1], [- 1], [0]])
        B = np.array([[1, 0], [0, 0], [0, - 1]])
        C1 = np.array([[1, 0, 1], [1, 0, 1]])
        C = np.array([1, 0, 0])
        D11 = np.zeros((2, 1))
        D21 = np.zeros((1, 1))
        D12 = np.array([[0, 1], [0, 0]])



    # ------------------------------------------------------------------
    # (DLR1): "Plate Experiment" for the active vibration damping of large
    #         flexible space structures, example of order 10
    #         J. Bals, "Aktive Schwingungsdaempfung flexibler Strukturen",
    #         Universitaet Karlsruhe, Fakultaet fuer Elektrotechnik,
    #         Germany, 1989
    #         reduced system
    # ------------------------------------------------------------------
    elif strmatch('DLR1', ex, 'exact'):
        nx = 10
        nu = 2
        ny = 2
        A = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [- 8.4268, 0, 9.6557, 0, - 5.083, - 0.0253, 0, 0.0155, 0, - 0.0112],
                      [0, - 20.2022, 0, 20.0736, 0, 0, - 0.0244, 0, 0.0151, 0],
                      [- 23.9425, 0, - 10.7354, 0, - 147.0685, - 0.0049, 0, - 0.0359, 0, - 0.0849],
                      [0, 126.1547, 0, - 132.8028, 0, 0, 0.0947, 0, - 0.1089, 0],
                      [- 39.905, 0, 6.607, 0, - 188.4411, - 0.0247, 0, 0.0016, 0, - 0.1368]])
        B = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [- 0.001, - 0.001], [- 0.0133, 0.0133], [0.048, 0.048],
                      [- 0.0516, 0.0516], [0.0213, 0.0213]])
        C = np.array([[0, 0, 0, 0, 0, 0.0115, - 0.0536, 0.9713, - 0.2009, - 0.5746],
                      [0, 0, 0, 0, 0, 0.0115, 0.0536, 0.9713, 0.2009, - 0.5746]])
        B1 = np.array(
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [- 0.0076, - 0.0076], [- 0.0351, 0.0351], [0.0972, 0.0972],
             [- 0.1824, 0.1824], [0.0748, 0.0748]])
        C1 = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [- 0.8084, 0, 0.7509, 0, - 0.9501, 0, 0, 0, 0, 0]])
        D12 = np.array([[1, 0], [0, 1]])
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D21 = np.array([[0, 0], [0.0972, 0.7509]])


    # ------------------------------------------------------------------
    # (ROC1): Four-disk control system
    #         K. Zhou, J. C. Doyle, K. Glover, "Robust and optimal control",
    #         Prentice Hall, 1996; p. 517, nc=1
    # ------------------------------------------------------------------
    elif strmatch('ROC1', ex, 'exact'):
        A = np.array([[- 0.161, - 6.004, - 0.58215, - 9.9835, - 0.40727, - 3.982, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]])
        B = np.array([[1], [0], [0], [0], [0], [0], [0], [0]])
        C = np.array([0, 0, 0.0064432, 0.0023196, 0.071252, 1.0002, 0.10455, 0.99551]).reshape((1, -1))
        q1 = 1e-06
        q2 = 1
        B1 = np.sqrt(q2) * np.array([[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
        C1 = np.sqrt(q1) * np.array([[0, 0, 0, 0, 0.55, 11, 1.32, 18], [0, 0, 0, 0, 0, 0, 0, 0]])
        D12 = np.array([[0], [1]])
        D21 = np.array([0, 1])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ------------------------------------------------------------------
    # (ROC2): Transport Aircraft model (Boing flight condition VFC/MFC)
    #         D. Gangsaas, K. R. Bruce, J. D. Blight and U.-L. Ly,
    #         "Application of Modern Synthesis to Aircraft Control:
    #         Three Case Studies", TOAC, Vol.31, Nr.11, pp.995-1014, 1986
    #         Case study III 1), nc=1
    # ------------------------------------------------------------------
    elif strmatch('ROC2', ex, 'exact'):
        A = np.array([[- 0.00702, 0.06339, 0.00518, - 0.55566, - 0.06112, 0, 0.00712, - 0.00566, 0],
                      [- 0.01654, - 0.38892, 1.0057, 0.00591, - 0.04632, 0, 0.01654, 0.04018, 0],
                      [0.00061, 0.3521, - 0.47381, 0, 1.7862, 0, - 0.00061, - 0.03638, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, - 20.0, 20, 0, 0, 0], [0, 0, 0, 0, 0, - 30, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, - 0.55454, 0, 0], [0, 0, 0, 0, 0, 0, 0, - 0.55454, 0.00555],
                      [0, 0, 0, 0, 0, 0, 0, - 0.00555, - 0.55454]])
        B = np.array([[0], [0], [0], [0], [0], [30], [0], [0], [0]])
        C = np.array([[0.005, 0.11679, - 0.00172, 0, - 0.01413, 0, - 0.005, - 0.01207, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]])

        B1 = np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1.0531, 0, 0, 0],
             [0, 1.28981, 0, 0], [0, - 54.514, 0, 0]])
        D12 = (1 / np.sqrt(2)) * np.array([1])
        D21 = np.array([[0, 0, 0, 0], [0, 0, 0, 1]])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        # nz, nx = C1.shape
        # D11 = np.zeros((nz, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        # C1 = np.array([C1, np.zeros((nz, nc))])
        # D12 = np.array([np.zeros((nz, nc)), D12])
        # D21 = np.array([[np.zeros((nc, nw))], [D21]])

    # --------------------------------------------------------------------
    # (ROC3): Output feedback problem: Wang and Rosenthal   ##ehemals (ROC8)
    #         "Output feedback pole placemant with dynamic compensatores"
    #         TOAC, vol.41, Nr. 6, pp. 830-843, 1996;  Example 3.21, nc=2
    # --------------------------------------------------------------------
    elif strmatch('ROC3', ex, 'exact'):
        A = np.array([[0, 0, 0, 0, 0, 0, 0, 0, - 1], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, - 1],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, - 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]])
        B = - np.array([[0, 1], [1, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1], [0, 0], [1, 0]])
        C = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]])
        nc = 2
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])

    # ------------------------------------------------------------------
    # (ROC4): Four disk control system
    #         D. S. Bernstein and W. M. Haddad, "LQG control with an H_inf
    #         performance bound: A Riccati equation approach",
    #         TOAC, Vol. 34, Nr. 3, pp. 293-305, 1989;   nc=1
    # ------------------------------------------------------------------
    elif strmatch('ROC4', ex, 'exact'):
        A = np.array([[- 0.161, 1, 0, 0, 0, 0, 0, 0], [- 6.004, 0, 1, 0, 0, 0, 0, 0], [- 0.5822, 0, 0, 1, 0, 0, 0, 0],
                      [- 9.9835, 0, 0, 0, 1, 0, 0, 0], [- 0.4073, 0, 0, 0, 0, 1, 0, 0], [- 3.982, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]])
        B = np.array([[0], [0], [0.0064], [0.00235], [0.0713], [1.002], [0.1045], [0.995]])
        C = np.array([1, 0, 0, 0, 0, 0, 0, 0]).reshape((1, -1))
        B1 = np.block([B, np.zeros((8, 1))])
        C1 = np.array([[0, 0, 0, 0, 0.55, 11, 1.32, 18], [0, 0, 0, 0, 0, 0, 0, 0]])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D12 = np.zeros((nz, nu))
        D21 = np.zeros((ny, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ------------------------------------------------------------------
    # (ROC5): Free Gyro-stabilized mirror system
    #         B. M. Chen, "H_inf Control and Its Applications",
    #         Springer-Verlag, "Lecture Notes in Control and Information Sciences",
    #         Vol.235, 1998; p. 310,  nc=1
    # ------------------------------------------------------------------
    elif strmatch('ROC5', ex, 'exact'):
        ab = 0.004
        bb = 0.00128
        cb = 0.00098
        db = 0.02
        eb = 0.0049
        fb = 0.0025
        gb = 0.00125
        lb = 0.0032
        kb = 0.0025
        th3 = 1
        psi1 = 0.011
        psi2 = 0.0011
        n1 = ab + bb + 0.5 * (eb + gb) + lb
        n2 = cb + 0.25 * fb + lb
        epsA = 5e-05
        A = np.array(
            [[0, 1, 0, 0, 0, 0], [0, 0, 0, - kb * th3 / n1, 0, 0], [0, 0, 0, 1, 0, 0], [0, kb * th3 / n2, 0, 0, 0, 0],
             [0, 0, 0, 0, - epsA, 0], [0, 0, 0, 0, 0, - epsA]])
        B = np.array([[0, 0], [1 / n1, 0], [0, 0], [0, 1 / n2], [0, 0], [0, 0]])
        C = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
        B1 = np.array([[0, 0, 0], [- 1, 0, 0], [0, 0, 0], [0, - 1, 0], [0, 0, psi1], [0, 0, psi2]])
        C1 = np.array([[1, 0, 0, 0, - 1, 0], [0, 0, 1, 0, 0, - 1]])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D12 = np.zeros((nz, nu))
        D21 = np.zeros((ny, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ------------------------------------------------------------------
    # (ROC6): P. Gahinet, "Reliable computation of H_inf central
    #         controllers near the optimum", Institut National de Recherche
    #         en Informatique et en Automatique, INRIA, Rocquencourt,
    #         1992; Example 7.3,   nc=2
    # ------------------------------------------------------------------
    elif strmatch('ROC6', ex, 'exact'):
        A = np.array([[1, - 1, 0], [1, 1, - 1], [0, 1, - 2]])
        B = np.array([[1], [0], [1]])
        C = np.array([0, - 1, 1]).reshape((1, -1))
        B1 = np.array([[1, 2, 0], [0, - 1, 0], [1, 1, 0]])
        C1 = np.array([[0, 0, 0], [1, 1, 0], [- 1, 0, 1]])
        D12 = np.array([[1], [0], [0]])
        D21 = np.array([0, 0, 1])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        nc = 2
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ------------------------------------------------------------------
    # (ROC7): Flexible actuator
    #         B. Fares, P. Apkarian and D. Noll,
    #         "An Augmented Lagrangian Method for a Class of LMI-Constrained
    #         Problems in Robust Control Theory",
    #         IJOC, Vol. 74, Nr. 4, pp. 348-360;  nc=1
    # ------------------------------------------------------------------
    elif strmatch('ROC7', ex, 'exact'):
        A = np.array([[0, 1, 0, 0], [- 1, 0, 0, 0], [0, 0, 0, 1.02], [0.2, 0, 0, 0]])
        B = np.array([[0], [- 0.2], [0], [1]])
        C = np.array([[1, 0, 0, 0], [0, 0, 1, 0]])
        C1 = np.array([[0.1, 0, 0, 0], [0, 0, 0.1, 0], [0, 0, 0, 0]])
        nz, nx = C1.shape
        B1 = np.array([[0], [1], [0], [- 0.2]])
        D12 = np.array([[0], [0], [0.2]])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D21 = np.zeros((ny, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ------------------------------------------------------------------
    # (ROC8): Augmented three mass spring system      ##ehemals (ROC3)
    #         L. El Ghaoui, F. Oustry and M. AitRami,
    #         "A cone complementarity linearization algorithm for static
    #         output feedback and related problems",
    #         TOAC, Vol. 42, Nr. 8, pp. 1171-1176, 1997;   nc=3
    # ------------------------------------------------------------------
    elif strmatch('ROC8', ex, 'exact'):
        k = 1
        A = np.array(
            [[0, 1, 0, 0, 0, 0], [- k, 0, k, 0, 0, 0], [0, 0, 0, 1, 0, 0],
             [k, 0, - 2 * k, 0, k, 0], [0, 0, 0, 0, 0, 1],
             [0, 0, k, 0, - k, 0]])
        B = np.array([[0], [1], [0], [0], [0], [0]])
        C = np.array([0, 0, 0, 0, 1, 0]).reshape((1, -1))
        B1 = np.array([[0], [0], [0], [0], [0], [1]])
        C1 = np.eye(6)
        CC = np.array([0, 0, 0, 0, 0, 0])
        C1 = np.block([[C1], [CC]])
        nx, nx = A.shape
        nx, nu = B.shape
        ny, nx = C.shape
        nx, nw = B1.shape
        nz, nx = C1.shape
        D11 = np.zeros((nz, nw))
        D12 = np.array([[0], [0], [0], [0], [0], [0], [1]])
        D21 = np.array([1])
        nc = 3
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # --------------------------------------------------------------------
    # (ROC9): Augmented two mass spring system
    #         M. Chilali and P. Gahinet, "H_inf design with pole placement
    #         constraints: An LMI approach", TOAC, Vol.41, Nr.3, pp.358-367
    # --------------------------------------------------------------------
    elif strmatch('ROC9', ex, 'exact'):
        k = 1
        A = np.array([[0, 1, 0, 0], [- k, 0, k, 0], [0, 0, 0, 1], [k, 0, - k, 0]])
        B1 = np.array([[0], [0], [0], [1]])
        B = np.array([[0], [1], [0], [0]])
        C1 = np.eye(4)
        CC = np.array([0, 0, 0, 0])
        C1 = np.block([[C1], [CC]])
        C = np.array([0, 0, 1, 0]).reshape((1, -1))
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D12 = np.array([[0], [0], [0], [0], [1]])
        D21 = np.array([1])
        nc = 2
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    # ----------------------------------------------------------------------
    # (ROC10): Inverted pendulum
    #          P. Apkarian and H. D. Tuan, "Robust Conrol via Concave
    #          Minimization, Local and Global Algorithms", TOAC, Vol. 45,
    #          Nr. 2, pp. 299-305, 2000; Ex. 1
    # ----------------------------------------------------------------------
    elif strmatch('ROC10', ex, 'exact'):
        A = np.array([[0, 1, 0, 0, 0], [48.9844, 0, - 48.9844, 0, 0], [0, 0, 0, 0.18494, 0], [0, 0, 0, - 50.0, 0],
                      [0, 0, - 0.5, 0, 0]])
        B1 = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0.5]])
        B = np.array([[0], [0], [50], [0], [0]])
        C1 = np.array([[0, 0, 0, 0.0036988, 0], [0, 0, 0, 0, 1]])
        C = np.array([[0, 0, 1, 0, 0], [1, 0, - 1, 0, 0], [0, 0, 0, 0, 1]])
        nx, nx = A.shape
        nx, nw = B1.shape
        nx, nu = B.shape
        nz, nx = C1.shape
        ny, nx = C.shape
        D11 = np.zeros((nz, nw))
        D12 = np.zeros((nz, nu))
        D21 = np.zeros((ny, nw))
        nc = 1
        A = np.block([[A, np.zeros((nx, nc))], [np.zeros((nc, nx)), np.zeros((nc, nc))]])
        B = np.block([[np.zeros((nx, nc)), B], [np.eye(nc), np.zeros((nc, nu))]])
        C = np.block([[np.zeros((nc, nx)), np.eye(nc)], [C, np.zeros((ny, nc))]])
        C1 = np.block([C1, np.zeros((nz, nc))])
        B1 = np.block([[B1], [np.zeros((nc, nw))]])
        D12 = np.block([np.zeros((nz, nc)), D12])
        D21 = np.block([[np.zeros((nc, nw))], [D21]])

    ##########################################################################

    # nx, nx = A.shape
    nx, nu = B.shape
    # ny, nx = C.shape

    # if len(B1) == 0:
    #     B1 = np.eye(nx)
    #     C1 = np.eye(nx)
    #     nx, nw = B1.shape
    #     nz, nx = C1.shape
    #     D12 = np.array([[np.zeros((nz - nu, nu))], [np.eye(nu)]])
    #     D11 = np.zeros((nz, nw))
    #     D21 = np.zeros((ny, nw))
    # else:
    #     nx, nw = B1.shape
    #     nz, nx = C1.shape
    #
    # ny = None
    # nw = None
    # nz = None

    return A, B1, B, C1, C, D11, D12, D21, nx, nw, nu, nz, ny
