from pytest import approx
import cfdverify.utils as utils
from cfdverify.discretization import Classic

def test_asme_procedure_phi1():
    """Test against ASME JFE annoucement
    
    This test tests the code against the data contained in the American Society
    of Mechanical Engineer's Journal of Fluids Engineering annoucement 
    "Procedure for Estimation and Reporting of Uncertainty Due to 
    Discretization in CFD Applications." Specifically, this test compares data 
    for the first response quantity, the dimensionless reattachement length.

    References
    ----------
    "Procedure for Estimation and Reporting of Uncertainty Due to 
    Discretization in CFD Applications." ASME. J. Fluids Eng. July 2008; 
    130(7): 078001. https://doi.org/10.1115/1.2960953
    """
    N = [18_000, 8_000, 4_500]
    V = 1 # placeholder volume
    mesh_sizes = utils.mesh_size(V, N, 2)
    phi1 = [6.063, 5.972, 5.863]
    model = Classic(mesh_sizes, phi1)
    assert model.refinement_ratios == approx([1.5, 1.333], abs=0.0005)
    assert model.order["System Response Quantity"] == approx(1.53, abs=0.005)
    assert model.f_est["System Response Quantity"] == approx(6.1685,
                                                             abs=0.00005)
    assert model.uncertainty("System Response Quantity", 0, normalize=True) == approx(0.022, abs=0.0005)

def test_asme_procedure_phi2():
    """Test against ASME JFE annoucement
    
    This test tests the code against the data contained in the American Society
    of Mechanical Engineer's Journal of Fluids Engineering annoucement 
    "Procedure for Estimation and Reporting of Uncertainty Due to 
    Discretization in CFD Applications." Specifically, this test compares data 
    for the second response quantity, the axial velocity at x/H=8 and y=0.0526.

    References
    ----------
    "Procedure for Estimation and Reporting of Uncertainty Due to 
    Discretization in CFD Applications." ASME. J. Fluids Eng. July 2008; 
    130(7): 078001. https://doi.org/10.1115/1.2960953
    """
    N = [18_000, 4_500, 980]
    V = 1 # placeholder volume
    mesh_sizes = utils.mesh_size(V, N, 2)
    phi1 = [10.7880, 10.7250, 10.6050]
    model = Classic(mesh_sizes, phi1)
    assert model.refinement_ratios == approx([2.0, 2.143], abs=0.0005)
    assert model.order["System Response Quantity"] == approx(0.75, abs=0.005)
    assert model.f_est["System Response Quantity"] == approx(10.8801,
                                                             abs=0.00005)
    assert model.uncertainty("System Response Quantity", 0, normalize=True) == approx(0.011, abs=0.0005)