# flake.nix
# https://www.youtube.com/watch?v=yQwW8dkuHqw
{
  description = "test";

  inputs =
    {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      system = "aarch64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.aarch64-darwin.default =
        pkgs.mkShell
          {
            nativeBuildInputs = with pkgs; [
              python313
            ];

            shellHook = ''
            fish
            '';

          };
    };
}
