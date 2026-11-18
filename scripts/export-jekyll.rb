require "json"
module FolioExport
  def convert(content)
    converted = super
    path = document.relative_path.sub(%r{\A/}, "")
    if document.is_a?(Jekyll::Page) && path.end_with?(".md")
      @folio_record = {
        "source" => path,
        "url" => document.url,
        "metadata" => document.data.select { |key, _| %w(title description parent grand_parent ancestor nav_order nav_exclude has_children layout permalink).include?(key) },
        "markdown" => content,
        "html" => converted
      }
      ($folio_export ||= {})[path] = @folio_record
    end
    converted
  end
end
Jekyll::Renderer.prepend(FolioExport)
Jekyll::Hooks.register :site, :post_write do |_site|
  File.write(ENV.fetch("FOLIO_EXPORT_PATH"), JSON.pretty_generate($folio_export), encoding: "UTF-8")
end
