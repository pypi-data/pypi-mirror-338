{ lib, python_pkgs, }:
lib.buildPythonPackage rec {
  pname = "grimp";
  version = "2.5";
  src = lib.fetchPypi {
    inherit pname version;
    sha256 = "korp/h39ReGAvKiz247IADqNOiOgnWE0a3CkcjisF2I=";
  };
  pythonImportsCheck = [ pname ];
  checkInputs = with python_pkgs; [ typing-extensions ];
}
