from project import get_numberOfTrips
from project import get_fueltype
from project import get_coordinates
from project import get_fuelConsumption
from project import get_fuelPrice
from project import generate_pdf
import pytest
import io
from os.path import exists



def test_get_numberOfTrips(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("2"))
    assert get_numberOfTrips() == 2

    monkeypatch.setattr("sys.stdin", io.StringIO("20"))
    assert get_numberOfTrips() == 20

    monkeypatch.setattr("sys.stdin", io.StringIO("ten"))
    with pytest.raises(EOFError):
         assert get_numberOfTrips()

    monkeypatch.setattr("sys.stdin", io.StringIO("2.5"))
    with pytest.raises(EOFError):
         assert get_numberOfTrips()

    monkeypatch.setattr("sys.stdin", io.StringIO("-5"))
    with pytest.raises(EOFError):
         assert get_numberOfTrips()



def test_get_fueltype(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("gas"))
    with pytest.raises(EOFError):
         assert get_fueltype()

    monkeypatch.setattr("sys.stdin", io.StringIO("500"))
    with pytest.raises(EOFError):
         assert get_fueltype()

    monkeypatch.setattr("sys.stdin", io.StringIO("Petrol"))
    assert get_fueltype() == "petrol"

    monkeypatch.setattr("sys.stdin", io.StringIO("peTrol"))
    assert get_fueltype() == "petrol"

    monkeypatch.setattr("sys.stdin", io.StringIO("PETROL"))
    assert get_fueltype() == "petrol"

    monkeypatch.setattr("sys.stdin", io.StringIO("Diesel"))
    assert get_fueltype() == "diesel"

    monkeypatch.setattr("sys.stdin", io.StringIO("DiEsel"))
    assert get_fueltype() == "diesel"

    monkeypatch.setattr("sys.stdin", io.StringIO("DIESEL"))
    assert get_fueltype() == "diesel"



def test_get_fuelConsumption(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("12"))
    assert get_fuelConsumption() == 12.0

    monkeypatch.setattr("sys.stdin", io.StringIO("10.5"))
    assert get_fuelConsumption() == 10.5

    monkeypatch.setattr("sys.stdin", io.StringIO("10.12345"))
    assert get_fuelConsumption() == 10.12345

    monkeypatch.setattr("sys.stdin", io.StringIO("gas"))
    with pytest.raises(EOFError):
         assert get_fuelConsumption()

    monkeypatch.setattr("sys.stdin", io.StringIO("-10"))
    with pytest.raises(EOFError):
         assert get_fuelConsumption()



def test_get_coordinates(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("OR Tambo international airport"))
    with pytest.raises(EOFError):
         assert get_coordinates("origin")

    monkeypatch.setattr("sys.stdin", io.StringIO("-91.92069865566052, 18.42130232958492"))
    with pytest.raises(EOFError):
         assert get_coordinates("origin")

    monkeypatch.setattr("sys.stdin", io.StringIO("-31.92069865566052, 182.42130232958492"))
    with pytest.raises(EOFError):
         assert get_coordinates("origin")

    monkeypatch.setattr("sys.stdin", io.StringIO("-33.920769878856504, 18.421431075606844"))
    assert get_coordinates("origin") == "-33.920769878856504, 18.421431075606844"

    monkeypatch.setattr("sys.stdin", io.StringIO("-26.109398704370616, 28.056128340820877"))
    assert get_coordinates("origin") == "-26.109398704370616, 28.056128340820877"

    monkeypatch.setattr("sys.stdin", io.StringIO("-29.726373513613176, 31.085350789835573"))
    assert get_coordinates("origin") == "-29.726373513613176, 31.085350789835573"



def test_get_fuelPrice(monkeypatch):
     monkeypatch.setattr("sys.stdin", io.StringIO("petrol"))
     assert get_fuelPrice("https://www.shell.co.za/motorists/shell-fuels/petrol-price.html") > 15

     monkeypatch.setattr("sys.stdin", io.StringIO("PETROL"))
     assert get_fuelPrice("https://www.shell.co.za/motorists/shell-fuels/petrol-price.html") > 15

     monkeypatch.setattr("sys.stdin", io.StringIO("diesel"))
     assert get_fuelPrice("https://www.shell.co.za/motorists/shell-fuels/petrol-price.html") > 15

     monkeypatch.setattr("sys.stdin", io.StringIO("DiEsel"))
     assert get_fuelPrice("https://www.shell.co.za/motorists/shell-fuels/petrol-price.html") > 15

     monkeypatch.setattr("sys.stdin", io.StringIO("jetfuel"))
     with pytest.raises(EOFError):
          assert get_fuelPrice("https://www.shell.co.za/motorists/shell-fuels/petrol-price.html")

     monkeypatch.setattr("sys.stdin", io.StringIO("petrol\n26"))
     assert get_fuelPrice("https://www.shell.co.za/motorist/shell-fuels/petrol-price.html") == 26

     monkeypatch.setattr("sys.stdin", io.StringIO("diesel\n200"))
     with pytest.raises(EOFError):
          assert get_fuelPrice("https://www.shell.co.za/motorist/shell-fuels/petrol-price.html")



def test_generate_pdf(monkeypatch, tmp_path):
     d = tmp_path / "dir"
     d.mkdir()
     testdata = ["Origin Address","Cape Town"]
     monkeypatch.setattr("sys.stdin", io.StringIO("yes"))
     generate_pdf(testdata)
     p = d / "cost_estimate.pdf"
     assert len(list(tmp_path.iterdir())) == 1
     assert exists("cost_estimate.pdf")

     monkeypatch.setattr("sys.stdin", io.StringIO("why"))
     with pytest.raises(EOFError):
          assert generate_pdf(testdata)

     monkeypatch.setattr("sys.stdin", io.StringIO("no"))
     assert generate_pdf(testdata) == None