namespace Sentinel.Web.Models.Engine;

public class HealthResponse
{
    public string Status { get; set; } = string.Empty;

    public string Service { get; set; } = string.Empty;

    public string Version { get; set; } = string.Empty;
}