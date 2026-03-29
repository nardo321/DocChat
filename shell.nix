{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python313
    pkgs.stdenv.cc.cc.lib  # Provides libstdc++.so.6
    pkgs.zlib              # Common dependency for compression
  ];

  shellHook = ''
    # This links the Nix store libraries to your environment
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH"
    
    # Automatically activate your venv if it exists
    if [ -d ".venv" ]; then
      source .venv/bin/activate
    fi
    
    echo "--- DocChat Environment Ready ---"
    echo "libstdc++ and zlib mapped to LD_LIBRARY_PATH"
  '';
}
