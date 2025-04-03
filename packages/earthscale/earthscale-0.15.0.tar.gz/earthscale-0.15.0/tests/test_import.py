def test_import() -> None:
    """
    Just checks whether we can import the module and all public symbols are
    still present.
    """
    import earthscale

    symbols = dir(earthscale)
    expected_symbols = [
        "EarthscaleClient",
        "DatasetType",
        "DatasetLabel",
        "SimpleDatasetMetadata",
        "FilenameBandPattern",
        "BaseAddDatasetRequest",
        "AddImageDatasetRequest",
        "AddVectorDatasetRequest",
        "AddZarrDatasetRequest",
        "AddTileServerDatasetRequest",
        "AddDatasetResponse",
        "AddDatasetRequest",
        "DatasetOverviewsStatus",
        "OptimizationStatus",
        "Optimization",
        "TileServer",
        "DatasetResponse",
        "Variable",
        "ListDatasetResponse",
        "EarthscaleClientError",
        "AuthenticationError",
        "NotFoundError",
        "ValidationFailedError",
        "TokenRefreshRequired",
        "VersionIncompatibleError",
    ]
    for symbol in expected_symbols:
        assert symbol in symbols
