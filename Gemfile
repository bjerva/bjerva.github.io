source "https://rubygems.org"

gem "github-pages", "~> 232", group: :jekyll_plugins

# Windows does not include zoneinfo files, so bundle the timezone data.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 2.0"
  gem "tzinfo-data"
end

# Support filesystem watching on Windows.
gem "wdm", "~> 0.1.0", :install_if => Gem.win_platform?
