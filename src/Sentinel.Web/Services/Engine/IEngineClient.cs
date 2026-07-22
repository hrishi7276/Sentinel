using Sentinel.Web.Models.Engine;

namespace Sentinel.Web.Services.Engine;

public interface IEngineClient
{
    Task<HealthResponse?> GetHealthAsync(
        CancellationToken cancellationToken = default);
}