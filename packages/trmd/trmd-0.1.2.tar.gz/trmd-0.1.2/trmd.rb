class Trmd < Formula
  include Language::Python::Virtualenv

  desc "Translate Markdown using OpenAI"
  homepage "https://github.com/rioriost/homebrew-trmd/"
  url "https://files.pythonhosted.org/packages/4c/fb/52767f59a84123cefa637c1bcd68bb6844747b2ead84b0910554790fc5d8/trmd-0.1.1.tar.gz"
  sha256 "6b932aec6cced4e52a8230c256794e62456edbd3e31c40336a58bb227bc71597"
  license "MIT"

  depends_on "python@3.13"

  def install
    virtualenv_install_with_resources
    system libexec/"bin/python", "-m", "pip", "install", "openai"
  end

  test do
    system "#{bin}/trmd", "--help"
  end
end
