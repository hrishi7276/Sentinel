using System.Net.Http.Json;
using Microsoft.Extensions.Options;
using Sentinel.Web.Configuration;
using Sentinel.Web.Models.Engine;

namespace Sentinel.Web.Services.Engine;

public class EngineClient : IEngineClient
{
    private readonly HttpClient _httpClient;

    public EngineClient(
        HttpClient httpClient,
        IOptions<EngineOptions> options)
    {
        _httpClient = httpClient;
        _httpClient.BaseAddress = new Uri(options.Value.BaseUrl);
    }

    public async Task<HealthResponse?> GetHealthAsync(
        CancellationToken cancellationToken = default)
    {
        return await _httpClient.GetFromJsonAsync<HealthResponse>(
            "/api/v1/health",
            cancellationToken);
    }
}